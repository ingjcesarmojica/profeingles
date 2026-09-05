/* ============================================================
   CHAT CON EL PROFESOR DE INGLES
   ============================================================ */

const chatMensajes = document.getElementById('chatMensajes');
const chatInput = document.getElementById('chatInput');
const chatSend = document.getElementById('chatSend');
const chatSugerencias = document.getElementById('chatSugerencias');

let nombreEstudiante = '';
let sesionIniciada = false;
let enEspera = false;

/** Agrega un mensaje del profesor al chat */
function agregarMensajeProfesor(texto) {
    const div = document.createElement('div');
    div.className = 'mensaje mensaje-profesor';
    div.innerHTML = `
        <div class="mensaje-autor">👨‍🏫 Profe Bilingue</div>
        <div class="mensaje-contenido">${formatear(texto)}</div>
    `;
    chatMensajes.appendChild(div);
    scrollAbajo();
}

/** Agrega un mensaje del alumno al chat */
function agregarMensajeAlumno(texto) {
    const div = document.createElement('div');
    div.className = 'mensaje mensaje-alumno';
    div.innerHTML = `
        <div class="mensaje-autor">${nombreEstudiante || 'Tú'}</div>
        <div class="mensaje-contenido">${formatear(texto)}</div>
    `;
    chatMensajes.appendChild(div);
    scrollAbajo();
}

/** Formatea texto con markdown simple (**negrita**) */
function formatear(texto) {
    if (!texto) return '';
    return texto
        .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
        .replace(/`(.+?)`/g, '<code>$1</code>')
        .replace(/\n/g, '<br>');
}

/** Hace scroll automatico al ultimo mensaje */
function scrollAbajo() {
    chatMensajes.scrollTop = chatMensajes.scrollHeight;
}

/** Envia un mensaje al profesor */
async function enviarMensaje(texto) {
    if (!texto.trim() || enEspera) return;

    agregarMensajeAlumno(texto);
    chatInput.value = '';
    enEspera = true;
    chatSend.disabled = true;

    try {
        // Si no hay sesion, primero pedimos el nombre
        if (!sesionIniciada) {
            if (!nombreEstudiante) {
                nombreEstudiante = texto.trim();
                if (!nombreEstudiante) {
                    agregarMensajeProfesor('Por favor escribe tu nombre para continuar.');
                    enEspera = false;
                    chatSend.disabled = false;
                    return;
                }
                // Iniciar sesion
                const resp = await fetch('/api/iniciar', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ nombre: nombreEstudiante, nivel: NIVEL_ID, leccion_id: LECCION_ID })
                });
                const data = await resp.json();
                if (data.error) {
                    agregarMensajeProfesor('❌ ' + data.error);
                    nombreEstudiante = '';
                } else {
                    sesionIniciada = true;
                    agregarMensajeProfesor(data.respuesta);
                    if (data.leccion && data.leccion.vocabulario) {
                        mostrarVocabPreview(data.leccion.vocabulario.slice(0, 3));
                    }
                }
            }
        } else {
            // Mensaje normal durante la sesion
            const resp = await fetch('/api/mensaje', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ mensaje: texto })
            });
            const data = await resp.json();
            if (data.error) {
                agregarMensajeProfesor('❌ ' + data.error);
            } else {
                agregarMensajeProfesor(data.respuesta);
                if (data.fin) {
                    // La sesion termino
                    setTimeout(() => {
                        agregarMensajeProfesor('👋 ¡Hasta pronto! Vuelve cuando quieras seguir aprendiendo.');
                    }, 1500);
                }
            }
        }
    } catch (err) {
        agregarMensajeProfesor('❌ Error de conexion. Intenta de nuevo.');
        console.error(err);
    } finally {
        enEspera = false;
        chatSend.disabled = false;
        chatInput.focus();
    }
}

/** Muestra un preview del vocabulario al inicio */
function mostrarVocabPreview(vocab) {
    let txt = '\n\n📚 Las primeras palabras que vamos a ver:\n';
    vocab.forEach(v => {
        txt += `  • ${v.ingles} = ${v.espanol}\n`;
    });
    setTimeout(() => {
        agregarMensajeProfesor(txt);
    }, 500);
}

// Event listeners
chatSend.addEventListener('click', () => {
    enviarMensaje(chatInput.value);
});

chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        enviarMensaje(chatInput.value);
    }
});

// Sugerencias rapidas
document.querySelectorAll('.sug-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const texto = btn.getAttribute('data-text');
        enviarMensaje(texto);
    });
});

// Mensaje de bienvenida automatico despues de 1 segundo
setTimeout(() => {
    agregarMensajeProfesor(
        `🎯 Hoy vamos a aprender: **${LECCION_NOMBRE}**\n` +
        `Nivel: **${NIVEL_NOMBRE}**\n\n` +
        `Mi metodología es simple: yo te explico todo en español, te muestro la palabra en inglés, ` +
        `y tú aprendes a asociarlas. Cuando estés listo/a, escribe tu **nombre** para empezar.`
    );
}, 800);

// Focus en el input
chatInput.focus();
