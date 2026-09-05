# 🇬🇧 Profesor de Inglés por Niveles (A1 → C2)

Aplicación web que enseña inglés a **hispanohablantes** siguiendo un orden lógico de niveles
según el **Marco Común Europeo de Referencia (MCER)**: A1, A2, B1, B2, C1, C2.

## ✨ Características principales

- **🌎 Enseña en español**: El profesor explica todo en español y muestra la equivalencia en inglés.
- **📚 55 lecciones estructuradas** en 6 niveles (de cero a avanzado).
- **🎯 Progresión lógica**: No saltas al siguiente nivel hasta dominar el actual.
- **💬 Chat interactivo**: El profesor te hace preguntas y evalúa tus respuestas.
- **📖 Vocabulario con pronunciación**: Guía fonética para hispanohablantes.
- **🧠 Evaluaciones por nivel**: Examen aleatorio con 10 preguntas para subir de nivel.
- **💾 Guardado de progreso**: SQLite local, sin requerir configuración adicional.
- **🎨 Diseño colorido**: Cada nivel tiene su color y emoji característicos.

## 📊 Estructura del curso

| Nivel | Nombre | Emoji | Lecciones | Enfoque |
|-------|--------|-------|-----------|---------|
| A1 | Principiante | 🌱 | 10 | Saludos, vocabulario básico, presente |
| A2 | Elemental | 🌿 | 10 | Rutinas, pasado simple, modales |
| B1 | Intermedio | 🌳 | 10 | Presente perfecto, opiniones, condicionales |
| B2 | Intermedio alto | 🎯 | 10 | Negocios, expresiones, voz pasiva |
| C1 | Avanzado | 🚀 | 10 | Argumentación, vocabulario sofisticado |
| C2 | Maestría | 👑 | 5 | Registro literario, filosófico, matices |

**Total: 55 lecciones con ~250+ palabras y ~200+ preguntas.**

## 🚀 Instalación

```bash
# 1. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. (Opcional) Configurar variables de entorno
cp .env.example .env
```

## ▶️ Ejecución

```bash
python app.py
```

Luego abre tu navegador en: **http://localhost:5000**

Al iniciar verás:

```
======================================================================
  PROFESOR DE INGLES POR NIVELES MCER (A1 -> C2)
  Ensenanza en espanol para hispanohablantes
======================================================================
  Total de lecciones: 55
    🌱 A1 - Principiante: 10 lecciones
    🌿 A2 - Elemental: 10 lecciones
    🌳 B1 - Intermedio: 10 lecciones
    🎯 B2 - Intermedio alto: 10 lecciones
    🚀 C1 - Avanzado: 10 lecciones
    👑 C2 - Maestria: 5 lecciones
======================================================================
  Servidor: http://localhost:5000
======================================================================
```

## 🎓 Cómo usar la aplicación

1. **Elige un nivel** en la página principal (te recomendamos empezar por A1 si no tienes base).
2. **Selecciona una lección** dentro del nivel.
3. **Escribe tu nombre** cuando el profesor te lo pida.
4. **Aprende el vocabulario**: el profesor te presenta cada palabra con:
   - Inglés: `Good morning`
   - Español: `Buenos días`
   - Pronunciación: `gud mor-ning`
5. **Practica con preguntas** escribiendo `practicar`.
6. **Responde en español o inglés** - el sistema acepta ambas formas.
7. **Avanza con `siguiente`** cuando hayas dominado la lección.

### Comandos disponibles en el chat

- `empezar` / `siguiente` - Avanza al siguiente contenido
- `practicar` - Pasa al modo de preguntas/evaluación
- `siguiente leccion` - Salta a la siguiente lección del nivel
- `siguiente nivel` - Sube al siguiente nivel (cuando completes todas las lecciones)
- `salir` - Termina la sesión

## 📁 Estructura del proyecto

```
profesor-ingles-niveles/
├── app.py                      # Aplicación Flask principal
├── database.py                 # Módulo de base de datos (SQLite)
├── data/
│   ├── __init__.py
│   └── temario.py              # Temario completo de los 6 niveles
├── templates/
│   ├── index.html              # Página principal (selector de nivel)
│   ├── nivel.html              # Vista de un nivel con sus lecciones
│   └── leccion.html            # Vista de lección con chat
├── static/
│   ├── css/
│   │   └── styles.css          # Estilos de la aplicación
│   └── js/
│       └── chat.js             # Lógica del chat con el profesor
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🛠️ API REST

La aplicación expone varias APIs para integraciones externas:

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/` | GET | Página principal |
| `/nivel/<nivel>` | GET | Vista de un nivel |
| `/leccion/<nivel>/<id>` | GET | Vista de una lección |
| `/api/niveles` | GET | Lista todos los niveles |
| `/api/lecciones/<nivel>` | GET | Lecciones de un nivel |
| `/api/leccion/<nivel>/<id>` | GET | Detalle de una lección |
| `/api/iniciar` | POST | Inicia sesión |
| `/api/mensaje` | POST | Envía mensaje al profesor |
| `/api/evaluacion/<nivel>` | GET | Genera 10 preguntas aleatorias |
| `/api/evaluacion/calificar` | POST | Califica evaluación |
| `/api/progreso/<nombre>` | GET | Progreso del estudiante |
| `/api/reset` | POST | Reinicia sesión |

## 🎯 Metodología pedagógica

El profesor sigue esta secuencia en cada lección:

1. **Presentación** - Saluda y explica el objetivo de la lección.
2. **Enseñanza** - Muestra el vocabulario con palabra en inglés, traducción y pronunciación.
3. **Práctica** - Hace preguntas para evaluar la comprensión.
4. **Corrección** - Celebra aciertos y corrige errores con suavidad.
5. **Avance** - Sugiere la siguiente lección o el siguiente nivel.

## 🌍 Idioma de la aplicación

- **Interfaz**: Español
- **Explicaciones del profesor**: Español
- **Palabras/frases enseñadas**: Inglés (con su equivalente en español)
- **Respuestas del usuario**: Español o inglés (el sistema es flexible)

## 💡 Diferencias con el proyecto original

Este proyecto es una **evolución completa** del proyecto base
`agentcallpingles-main` (que era un agente para llamadas por teléfono):

| Característica | agentcallpingles-main | profesor-ingles-niveles |
|---|---|---|
| Niveles cubiertos | Solo A1 | A1, A2, B1, B2, C1, C2 (55 lecciones) |
| Idioma del agente | Español | Español (más consistente) |
| Interfaz | Teléfono (TTS) | Web responsive |
| Base de datos | Supabase | SQLite local (más simple) |
| Progresión | Por llamada | Por niveles con evaluación |
| Evaluaciones | ❌ | ✅ 10 preguntas por nivel |
| Vocabulario | ~70 palabras | ~300+ palabras |
| Preguntas | ~30 | ~200+ preguntas |

## 📝 Licencia

Proyecto educativo de uso libre.

---

**💡 Hecho con ❤️ para hispanohablantes que quieren aprender inglés de forma ordenada y clara.**

