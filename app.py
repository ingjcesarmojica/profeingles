"""
Profesor de Ingles - Aplicacion Web
====================================
Enseña ingles a hispanohablantes en orden logico de niveles MCER:
A1 -> A2 -> B1 -> B2 -> C1 -> C2
"""
import os
import re
import json
import random
import logging
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from data.temario import (
    ORDEN_NIVELES, obtener_niveles, obtener_info_nivel,
    obtener_lecciones_nivel, obtener_leccion, total_lecciones_nivel,
    total_lecciones_todos, siguiente_nivel, validar_respuesta,
    siguiente_pregunta_aleatoria, obtener_siguiente_leccion
)
from database import (
    guardar_estudiante, obtener_estudiante, actualizar_progreso,
    guardar_conversacion, guardar_evaluacion
)

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "profesor-ingles-secret-2026")
CORS(app)
logging.basicConfig(level=logging.INFO)

# Estado de sesiones
session_states = {}


def get_session_state(sid="default"):
    if sid not in session_states:
        session_states[sid] = {
            "paso": "inicio", "nivel": "A1", "leccion_id": None,
            "vocab_index": 0, "preguntas_respondidas": [],
            "aciertos_seguidos": 0, "aciertos_total": 0,
            "errores_total": 0, "pregunta_actual": None,
            "pregunta_indice": None, "nombre": "",
        }
    return session_states[sid]


def reset_session(sid="default"):
    if sid in session_states:
        del session_states[sid]
    return get_session_state(sid)


# ============================================================
# RUTAS PRINCIPALES (HTML)
# ============================================================

@app.route("/")
def index():
    """Pagina principal - selector de nivel"""
    niveles_info = []
    for nivel_id in ORDEN_NIVELES:
        info = obtener_info_nivel(nivel_id)
        niveles_info.append({
            "id": nivel_id,
            "nombre": info["nombre"],
            "descripcion": info["descripcion"],
            "color": info["color"],
            "emoji": info["emoji"],
            "total_lecciones": total_lecciones_nivel(nivel_id),
        })
    return render_template("index.html", niveles=niveles_info, total=total_lecciones_todos())


@app.route("/nivel/<nivel>")
def nivel(nivel):
    """Vista de un nivel especifico con sus lecciones"""
    info = obtener_info_nivel(nivel)
    if not info:
        return "Nivel no encontrado", 404
    lecciones = obtener_lecciones_nivel(nivel)
    lecciones_resumen = []
    for i, lec in enumerate(lecciones, 1):
        lecciones_resumen.append({
            "id": lec["id"],
            "numero": i,
            "nombre": lec["nombre"],
            "objetivo": lec.get("objetivo", ""),
            "vocab_count": len(lec.get("vocabulario", [])),
            "preguntas_count": len(lec.get("preguntas", [])),
        })
    return render_template("nivel.html",
                           nivel_id=nivel,
                           nivel_info=info,
                           lecciones=lecciones_resumen,
                           total=len(lecciones_resumen))


@app.route("/leccion/<nivel>/<leccion_id>")
def leccion(nivel, leccion_id):
    """Vista de una leccion especifica con el profesor"""
    lec = obtener_leccion(nivel, leccion_id)
    if not lec:
        return "Leccion no encontrada", 404
    info_nivel = obtener_info_nivel(nivel)
    prox_leccion = obtener_siguiente_leccion(nivel, leccion_id)
    return render_template("leccion.html",
                           nivel_id=nivel,
                           nivel_info=info_nivel,
                           leccion=lec,
                           proxima=prox_leccion["id"] if prox_leccion else None,
                           es_ultima=prox_leccion is None)


# ============================================================
# API - INICIAR SESION
# ============================================================

@app.route("/api/iniciar", methods=["POST"])
def iniciar_sesion():
    data = request.json or {}
    nombre = (data.get("nombre") or "").strip()
    nivel = (data.get("nivel") or "A1").upper()
    leccion_id = data.get("leccion_id")

    if not nombre:
        return jsonify({"error": "Por favor dime tu nombre"}), 400
    if nivel not in ORDEN_NIVELES:
        return jsonify({"error": "Nivel invalido"}), 400

    sid = request.remote_addr or "default"
    state = reset_session(sid)
    state["nombre"] = nombre
    state["nivel"] = nivel
    guardar_estudiante(nombre)

    lecciones = obtener_lecciones_nivel(nivel)
    if not lecciones:
        return jsonify({"error": "Nivel sin lecciones"}), 400
    if leccion_id and obtener_leccion(nivel, leccion_id):
        state["leccion_id"] = leccion_id
    else:
        state["leccion_id"] = lecciones[0]["id"]
    state["paso"] = "presentacion"

    lec = obtener_leccion(nivel, state["leccion_id"])
    info = obtener_info_nivel(nivel)

    bienvenida = (
        f"¡Hola {nombre}! 👋 Bienvenido/a al nivel {info['nombre']}.\n\n"
        f"Ahora vamos a estudiar: **{lec['nombre']}**\n"
        f"Objetivo: {lec.get('objetivo', 'Aprender nuevo vocabulario')}\n\n"
        f"Te voy a ensenar en espanol y tu aprendes como se dice en ingles. "
        f"Escribe 'empezar' o 'siguiente' para ver la primera palabra."
    )

    state["ultima_respuesta"] = bienvenida
    guardar_conversacion(nombre, nivel, state["leccion_id"], "presentacion", "", bienvenida, None)
    return jsonify({
        "respuesta": bienvenida,
        "leccion": lec,
        "nivel": info,
        "paso": state["paso"]
    })


# ============================================================
# API - MENSAJES DEL ALUMNO
# ============================================================

@app.route("/api/mensaje", methods=["POST"])
def mensaje():
    data = request.json or {}
    sid = request.remote_addr or "default"
    state = get_session_state(sid)
    mensaje_usuario = (data.get("mensaje") or "").strip()
    nombre = state.get("nombre") or "Estudiante"
    nivel = state["nivel"]
    leccion_id = state["leccion_id"]

    if not mensaje_usuario:
        return jsonify({"error": "Mensaje vacio"}), 400

    lec = obtener_leccion(nivel, leccion_id)
    if not lec:
        return jsonify({"error": "Leccion no encontrada"}), 404

    msg_lower = mensaje_usuario.lower().strip()

    # Comando: Salir
    if msg_lower in ["salir", "terminar", "adios", "bye", "chao", "exit", "quit"]:
        respuesta = (
            f"¡Muy bien {nombre}! Hoy avanzamos mucho. 👏\n"
            f"Llevas {state['aciertos_total']} aciertos en esta sesion.\n"
            f"Nos vemos pronto. ¡Sigue practicando! (See you soon!)"
        )
        guardar_conversacion(nombre, nivel, leccion_id, "fin", mensaje_usuario, respuesta, None)
        return jsonify({"respuesta": respuesta, "paso": "fin", "fin": True})

    # Comandos de avance
    if msg_lower in ["empezar", "siguiente", "next", "continuar", "start", "comenzar", "go"]:
        if state["paso"] in ["presentacion", "completada"]:
            state["paso"] = "ensenando"
            state["vocab_index"] = 0
            state["preguntas_respondidas"] = []
            state["aciertos_seguidos"] = 0
            return _presentar_vocabulario(state, lec)
        if state["paso"] == "ensenando":
            state["vocab_index"] = state.get("vocab_index", 0) + 1
            return _presentar_vocabulario(state, lec)
        if state["paso"] == "preguntando":
            return _nueva_pregunta(state, lec)

    # Ensenando vocabulario
    if state["paso"] == "ensenando":
        if msg_lower in ["ya", "listo", "ok", "entendido", "siguiente palabra", "next word"]:
            state["vocab_index"] = state.get("vocab_index", 0) + 1
            return _presentar_vocabulario(state, lec)
        if msg_lower in ["practicar", "preguntame", "evaluar", "test", "practica"]:
            state["paso"] = "preguntando"
            return _nueva_pregunta(state, lec)
        idx = state.get("vocab_index", 0)
        if idx < len(lec["vocabulario"]):
            p = lec["vocabulario"][idx]
            respuesta = (
                f"👍 Estas aprendiendo: **{p['ingles']}** ({p['espanol']}).\n"
                f"Pronunciacion: {p['pronunciacion']}\n"
                f"Repitelo en voz alta o escribe 'siguiente' para otra palabra, "
                f"o 'practicar' cuando quieras que te pregunte."
            )
        else:
            respuesta = "Escribe 'practicar' para que te haga preguntas sobre esta leccion."
        guardar_conversacion(nombre, nivel, leccion_id, "ensenando", mensaje_usuario, respuesta, None)
        return jsonify({"respuesta": respuesta, "paso": state["paso"]})

    # Respondiendo preguntas
    if state["paso"] == "preguntando":
        pregunta = state.get("pregunta_actual")
        if not pregunta:
            return _nueva_pregunta(state, lec)

        es_correcto = validar_respuesta(mensaje_usuario, pregunta)
        if es_correcto:
            state["aciertos_seguidos"] += 1
            state["aciertos_total"] += 1
            state["preguntas_respondidas"].append(state.get("pregunta_indice"))
            respuesta = f"¡Excelente! 🎉 ¡Correcto! La respuesta es **{pregunta['respuesta_correcta']}**.\n"
            if len(state["preguntas_respondidas"]) >= len(lec["preguntas"]):
                state["paso"] = "completada"
                actualizar_progreso(nombre, nivel, leccion_id, completada=True)
                prox = obtener_siguiente_leccion(nivel, leccion_id)
                if prox:
                    respuesta += (
                        f"\n✅ ¡Leccion completada! Has dominado **{lec['nombre']}**.\n"
                        f"Siguiente: **{prox['nombre']}** - escribe 'siguiente' para continuar."
                    )
                else:
                    sig_nivel = siguiente_nivel(nivel)
                    if sig_nivel:
                        respuesta += (
                            f"\n🎉 ¡FELICIDADES! Completaste el nivel {nivel}.\n"
                            f"Listo para **{sig_nivel}** - escribe 'siguiente nivel'."
                        )
                    else:
                        respuesta += "\n🏆 ¡Completaste todos los niveles (A1-C2)!"
            else:
                idx, nueva = siguiente_pregunta_aleatoria(lec, state["preguntas_respondidas"])
                if nueva:
                    state["pregunta_indice"] = idx
                    state["pregunta_actual"] = nueva
                    respuesta += f"Siguiente: {nueva['pregunta']}"
                else:
                    state["paso"] = "completada"
            guardar_conversacion(nombre, nivel, leccion_id, state["paso"], mensaje_usuario, respuesta, True)
            return jsonify({"respuesta": respuesta, "paso": state["paso"], "acierto": True})
        else:
            state["aciertos_seguidos"] = 0
            state["errores_total"] += 1
            pista = pregunta.get("pista", "")
            respuesta = (
                f"Casi. ❌ La respuesta correcta es: **{pregunta['respuesta_correcta']}**.\n"
                f"Pista: {pista}\n"
                f"Intentalo de nuevo: {pregunta['pregunta']}"
            )
            guardar_conversacion(nombre, nivel, leccion_id, "preguntando", mensaje_usuario, respuesta, False)
            return jsonify({"respuesta": respuesta, "paso": state["paso"], "acierto": False})

    # Leccion completada
    if state["paso"] == "completada":
        if "siguiente nivel" in msg_lower or "cambiar nivel" in msg_lower:
            sig_nivel = siguiente_nivel(nivel)
            if sig_nivel:
                state["nivel"] = sig_nivel
                lecciones = obtener_lecciones_nivel(sig_nivel)
                state["leccion_id"] = lecciones[0]["id"]
                state["paso"] = "presentacion"
                info = obtener_info_nivel(sig_nivel)
                respuesta = (
                    f"🎓 Bienvenido al nivel **{info['nombre']}** {info['emoji']}\n"
                    f"{info['descripcion']}\n"
                    f"Primera leccion: {lecciones[0]['nombre']}\n"
                    f"Escribe 'empezar' cuando estes listo/a."
                )
                guardar_conversacion(nombre, sig_nivel, lecciones[0]["id"], "presentacion", mensaje_usuario, respuesta, None)
                return jsonify({"respuesta": respuesta, "paso": state["paso"], "nivel": info})
        if "siguiente" in msg_lower:
            prox = obtener_siguiente_leccion(nivel, leccion_id)
            if prox:
                state["leccion_id"] = prox["id"]
                state["paso"] = "ensenando"
                state["vocab_index"] = 0
                state["preguntas_respondidas"] = []
                state["aciertos_seguidos"] = 0
                nueva_lec = obtener_leccion(nivel, prox["id"])
                respuesta = (
                    f"📚 Nueva leccion: **{nueva_lec['nombre']}**\n"
                    f"Objetivo: {nueva_lec.get('objetivo', '')}\n\n"
                    f"Palabras a aprender:\n"
                )
                for v in nueva_lec["vocabulario"][:3]:
                    respuesta += f"  - {v['ingles']} ({v['pronunciacion']}) = {v['espanol']}\n"
                respuesta += "\nEscribe 'siguiente' para mas palabras o 'practicar' cuando estes listo/a."
                guardar_conversacion(nombre, nivel, prox["id"], "ensenando", mensaje_usuario, respuesta, None)
                return jsonify({"respuesta": respuesta, "paso": state["paso"], "leccion": nueva_lec})
        respuesta = (
            f"Ya terminaste esta leccion. ✅\n"
            f"Escribe 'siguiente leccion' para avanzar, o 'siguiente nivel' para subir de nivel."
        )
        guardar_conversacion(nombre, nivel, leccion_id, state["paso"], mensaje_usuario, respuesta, None)
        return jsonify({"respuesta": respuesta, "paso": state["paso"]})

    # Fallback
    respuesta = (
        "🤔 No estoy seguro de que quisiste decir.\n"
        "Comandos utiles: 'empezar', 'siguiente', 'practicar', "
        "'siguiente leccion', 'siguiente nivel', 'salir'."
    )
    guardar_conversacion(nombre, nivel, leccion_id, state["paso"], mensaje_usuario, respuesta, None)
    return jsonify({"respuesta": respuesta, "paso": state["paso"]})


def _presentar_vocabulario(state, lec):
    """Presenta una palabra de vocabulario"""
    idx = state.get("vocab_index", 0)
    if idx >= len(lec["vocabulario"]):
        state["paso"] = "preguntando"
        return _nueva_pregunta(state, lec)
    palabra = lec["vocabulario"][idx]
    respuesta = (
        f"📖 Palabra {idx + 1} de {len(lec['vocabulario'])}:\n\n"
        f"**Ingles:** {palabra['ingles']}\n"
        f"**Espanol:** {palabra['espanol']}\n"
        f"**Pronunciacion:** {palabra['pronunciacion']}\n\n"
        f"💡 Repitelo en voz alta varias veces.\n"
        f"Escribe 'siguiente' para otra palabra, o 'practicar' para evaluacion."
    )
    guardar_conversacion(state.get("nombre", ""), state["nivel"], state["leccion_id"],
                          "ensenando", "", respuesta, None)
    return jsonify({
        "respuesta": respuesta,
        "paso": state["paso"],
        "palabra": palabra,
        "progreso": f"{idx + 1}/{len(lec['vocabulario'])}"
    })


def _nueva_pregunta(state, lec):
    """Selecciona y presenta una nueva pregunta aleatoria"""
    if not lec.get("preguntas"):
        state["paso"] = "completada"
        return jsonify({
            "respuesta": "Esta leccion no tiene preguntas. Escribe 'siguiente leccion'.",
            "paso": state["paso"]
        })
    idx, pregunta = siguiente_pregunta_aleatoria(lec, state.get("preguntas_respondidas"))
    if not pregunta:
        state["paso"] = "completada"
        prox = obtener_siguiente_leccion(state["nivel"], state["leccion_id"])
        if prox:
            respuesta = f"🎉 ¡Completaste todas las preguntas! Siguiente: **{prox['nombre']}** - escribe 'siguiente leccion'."
        else:
            respuesta = "🎉 ¡Completaste todas las preguntas! Escribe 'siguiente nivel'."
        guardar_conversacion(state.get("nombre", ""), state["nivel"], state["leccion_id"],
                              "completada", "", respuesta, None)
        return jsonify({"respuesta": respuesta, "paso": state["paso"]})

    state["pregunta_indice"] = idx
    state["pregunta_actual"] = pregunta
    respuesta = f"🎯 Vamos a practicar:\n\n**{pregunta['pregunta']}**"
    guardar_conversacion(state.get("nombre", ""), state["nivel"], state["leccion_id"],
                          "preguntando", "", respuesta, None)
    return jsonify({
        "respuesta": respuesta,
        "paso": state["paso"],
        "pregunta": pregunta
    })


# ============================================================
# API AUXILIARES
# ============================================================

@app.route("/api/niveles", methods=["GET"])
def api_niveles():
    return jsonify({
        "niveles": [{
            "id": n,
            **obtener_info_nivel(n),
            "total_lecciones": total_lecciones_nivel(n)
        } for n in ORDEN_NIVELES],
        "total_lecciones": total_lecciones_todos()
    })


@app.route("/api/lecciones/<nivel>", methods=["GET"])
def api_lecciones(nivel):
    lecciones = obtener_lecciones_nivel(nivel)
    return jsonify({
        "nivel": nivel,
        "lecciones": [{
            "id": l["id"], "nombre": l["nombre"],
            "objetivo": l.get("objetivo", ""),
            "vocabulario": l.get("vocabulario", []),
            "preguntas_count": len(l.get("preguntas", []))
        } for l in lecciones],
        "total": len(lecciones)
    })


@app.route("/api/leccion/<nivel>/<leccion_id>", methods=["GET"])
def api_leccion(nivel, leccion_id):
    lec = obtener_leccion(nivel, leccion_id)
    if not lec:
        return jsonify({"error": "Leccion no encontrada"}), 404
    return jsonify(lec)


@app.route("/api/evaluacion/<nivel>", methods=["GET"])
def api_evaluacion(nivel):
    """Genera preguntas aleatorias para evaluar el nivel"""
    lecciones = obtener_lecciones_nivel(nivel)
    if not lecciones:
        return jsonify({"error": "Nivel sin lecciones"}), 404
    todas_preguntas = []
    for lec in lecciones:
        for p in lec.get("preguntas", []):
            todas_preguntas.append({
                "leccion_id": lec["id"],
                "leccion_nombre": lec["nombre"],
                **p
            })
    sample = random.sample(todas_preguntas, min(10, len(todas_preguntas)))
    return jsonify({"nivel": nivel, "preguntas": sample, "total": len(sample)})


@app.route("/api/evaluacion/calificar", methods=["POST"])
def api_calificar():
    data = request.json or {}
    nombre = data.get("nombre", "")
    nivel = data.get("nivel", "")
    respuestas = data.get("respuestas", [])
    preguntas = data.get("preguntas", [])
    correctas = 0
    for r in respuestas:
        pidx = r.get("indice")
        if pidx is not None and pidx < len(preguntas):
            if validar_respuesta(r.get("respuesta", ""), preguntas[pidx]):
                correctas += 1
    total = len(preguntas)
    aprobado = correctas >= (total * 0.7)
    if nombre and nivel:
        guardar_evaluacion(nombre, nivel, correctas, total, aprobado)
    return jsonify({
        "puntaje": correctas,
        "total": total,
        "porcentaje": round((correctas / total) * 100, 1) if total > 0 else 0,
        "aprobado": aprobado,
        "siguiente_nivel": siguiente_nivel(nivel) if aprobado else None
    })


@app.route("/api/progreso/<nombre>", methods=["GET"])
def api_progreso(nombre):
    est = obtener_estudiante(nombre)
    if not est:
        return jsonify({"error": "Estudiante no encontrado"}), 404
    return jsonify(est)


@app.route("/api/reset", methods=["POST"])
def api_reset():
    sid = request.remote_addr or "default"
    reset_session(sid)
    return jsonify({"status": "ok", "mensaje": "Sesion reiniciada"})


# ============================================================
# INICIO
# ============================================================

if __name__ == "__main__":
    import sys
    if sys.platform.startswith("win"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    port = int(os.environ.get("PORT", 5000))
    print("=" * 70)
    print("  PROFESOR DE INGLES POR NIVELES MCER (A1 -> C2)")
    print("  Ensenanza en espanol para hispanohablantes")
    print("=" * 70)
    print(f"  Total de lecciones: {total_lecciones_todos()}")
    for n in ORDEN_NIVELES:
        info = obtener_info_nivel(n)
        emoji = info.get("emoji", "")
        print(f"    {emoji} {info['nombre']}: {total_lecciones_nivel(n)} lecciones")
    print("=" * 70)
    print(f"  Servidor: http://localhost:{port}")
    print("=" * 70)
    app.run(host="0.0.0.0", port=port, debug=False)





