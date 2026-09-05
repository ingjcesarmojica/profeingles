"""
Modulo de base de datos para el Profesor de Ingles
Soporta dos modos:
  - JSON local (por defecto, no requiere instalacion extra)
  - Supabase (opcional, si se quiere usar en la nube)
"""
import os
import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "profesor_ingles.db"

USE_SUPABASE = bool(os.environ.get("SUPABASE_URL") and os.environ.get("SUPABASE_KEY"))


def _get_conn():
    """Obtiene una conexion a SQLite"""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Crea las tablas si no existen"""
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            nivel_actual TEXT DEFAULT 'A1',
            leccion_actual TEXT,
            lecciones_completadas TEXT DEFAULT '{}',
            fecha_creacion TEXT,
            ultima_actividad TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS conversaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            nivel TEXT,
            leccion_id TEXT,
            paso TEXT,
            mensaje_usuario TEXT,
            respuesta_agente TEXT,
            acierto INTEGER,
            timestamp TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS evaluaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            nivel TEXT,
            puntaje INTEGER,
            total_preguntas INTEGER,
            aprobado INTEGER,
            fecha TEXT
        )
    """)
    conn.commit()
    conn.close()


def guardar_estudiante(nombre: str) -> bool:
    """Crea un estudiante nuevo si no existe"""
    conn = _get_conn()
    try:
        conn.execute(
            "INSERT INTO estudiantes (nombre, fecha_creacion, ultima_actividad) VALUES (?, ?, ?)",
            (nombre, datetime.now().isoformat(), datetime.now().isoformat())
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def obtener_estudiante(nombre: str) -> Optional[Dict]:
    """Obtiene un estudiante por su nombre"""
    conn = _get_conn()
    row = conn.execute("SELECT * FROM estudiantes WHERE nombre = ?", (nombre,)).fetchone()
    conn.close()
    if row:
        d = dict(row)
        try:
            d["lecciones_completadas"] = json.loads(d.get("lecciones_completadas") or "{}")
        except Exception:
            d["lecciones_completadas"] = {}
        return d
    return None


def actualizar_progreso(nombre: str, nivel: str, leccion_id: str, completada: bool = False) -> None:
    """Actualiza el progreso del estudiante"""
    conn = _get_conn()
    estudiante = conn.execute("SELECT lecciones_completadas FROM estudiantes WHERE nombre = ?",
                              (nombre,)).fetchone()
    if not estudiante:
        conn.close()
        return
    try:
        completadas = json.loads(estudiante["lecciones_completadas"] or "{}")
    except Exception:
        completadas = {}
    if nivel not in completadas:
        completadas[nivel] = []
    if completada and leccion_id not in completadas[nivel]:
        completadas[nivel].append(leccion_id)
    conn.execute(
        "UPDATE estudiantes SET nivel_actual=?, leccion_actual=?, lecciones_completadas=?, ultima_actividad=? WHERE nombre=?",
        (nivel, leccion_id, json.dumps(completadas), datetime.now().isoformat(), nombre)
    )
    conn.commit()
    conn.close()


def guardar_conversacion(nombre: str, nivel: str, leccion_id: str, paso: str,
                          mensaje_usuario: str, respuesta_agente: str, acierto: bool = None) -> None:
    """Guarda un turno de la conversacion"""
    conn = _get_conn()
    conn.execute(
        """INSERT INTO conversaciones (nombre, nivel, leccion_id, paso, mensaje_usuario,
                                       respuesta_agente, acierto, timestamp)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (nombre, nivel, leccion_id, paso, mensaje_usuario, respuesta_agente,
         int(acierto) if acierto is not None else None, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


def guardar_evaluacion(nombre: str, nivel: str, puntaje: int, total: int, aprobado: bool) -> None:
    """Registra el resultado de una evaluacion"""
    conn = _get_conn()
    conn.execute(
        "INSERT INTO evaluaciones (nombre, nivel, puntaje, total_preguntas, aprobado, fecha) VALUES (?, ?, ?, ?, ?, ?)",
        (nombre, nivel, puntaje, total, int(aprobado), datetime.now().isoformat())
    )
    conn.commit()
    conn.close()


def obtener_historial(nombre: str, limite: int = 20) -> List[Dict]:
    """Obtiene el historial reciente de conversaciones de un estudiante"""
    conn = _get_conn()
    rows = conn.execute(
        "SELECT * FROM conversaciones WHERE nombre = ? ORDER BY id DESC LIMIT ?",
        (nombre, limite)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# Inicializar la BD al cargar el modulo
init_db()
