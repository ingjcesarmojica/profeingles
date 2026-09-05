"""
Temario completo del curso de ingles por niveles MCER
Marco Comun Europeo de Referencia: A1, A2, B1, B2, C1, C2
"""
import re, random

# ============================================================
# NIVEL A1 - Principiante (Acceso)
# ============================================================
TEMARIO_A1 = [
    {
        "id": "A1-01", "nivel": "A1", "nombre": "Saludos y despedidas",
        "objetivo": "Aprender a saludar y despedirse en ingles de forma formal e informal",
        "vocabulario": [
            {"ingles": "Hello", "pronunciacion": "je-lou", "espanol": "Hola (formal)"},
            {"ingles": "Hi", "pronunciacion": "jai", "espanol": "Hola (informal)"},
            {"ingles": "Good morning", "pronunciacion": "gud mor-ning", "espanol": "Buenos dias"},
            {"ingles": "Good afternoon", "pronunciacion": "gud af-ter-nun", "espanol": "Buenas tardes"},
            {"ingles": "Good evening", "pronunciacion": "gud iv-ning", "espanol": "Buenas noches (al llegar)"},
            {"ingles": "Goodbye", "pronunciacion": "gud-bai", "espanol": "Adios (formal)"},
            {"ingles": "Bye", "pronunciacion": "bai", "espanol": "Adios (informal)"},
            {"ingles": "Please", "pronunciacion": "plis", "espanol": "Por favor"},
            {"ingles": "Thank you", "pronunciacion": "zank iu", "espanol": "Gracias"},
            {"ingles": "Sorry", "pronunciacion": "so-ri", "espanol": "Disculpa / Lo siento"},
        ],
        "preguntas": [
            {"pregunta": "Como se dice 'Hola' (informal) en ingles?", "respuesta_correcta": "hi",
             "alternativas": ["hi", "hello"], "pista": "Es una palabra muy corta, de 2 letras."},
            {"pregunta": "Como se dice 'Buenos dias' en ingles?", "respuesta_correcta": "good morning",
             "alternativas": ["good morning"], "pista": "good = bueno, morning = manana."},
            {"pregunta": "Que significa 'goodbye'?", "respuesta_correcta": "adios",
             "alternativas": ["adios", "hasta luego"], "pista": "Es una despedida formal."},
            {"pregunta": "Como se dice 'Por favor' en ingles?", "respuesta_correcta": "please",
             "alternativas": ["please", "plis"], "pista": "Empieza con P."},
            {"pregunta": "Que significa 'thank you'?", "respuesta_correcta": "gracias",
             "alternativas": ["gracias"], "pista": "Lo dices cuando recibes algo."},
        ],
    },
    {
        "id": "A1-02", "nivel": "A1", "nombre": "Presentarse",
        "objetivo": "Decir tu nombre, edad y de donde eres",
        "vocabulario": [
            {"ingles": "My name is...", "pronunciacion": "mai neim is", "espanol": "Mi nombre es..."},
            {"ingles": "I am...", "pronunciacion": "ai am", "espanol": "Yo soy / Yo estoy..."},
            {"ingles": "What is your name?", "pronunciacion": "uot is ior neim", "espanol": "Como te llamas?"},
            {"ingles": "Nice to meet you", "pronunciacion": "nais tu mit iu", "espanol": "Mucho gusto"},
            {"ingles": "I am from...", "pronunciacion": "ai am from", "espanol": "Soy de..."},
            {"ingles": "I am ... years old", "pronunciacion": "ai am ... iers old", "espanol": "Tengo ... anos"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'Mi nombre es' en ingles?", "respuesta_correcta": "my name is",
             "alternativas": ["my name is"], "pista": "my = mi, name = nombre, is = es."},
            {"pregunta": "Como preguntas 'Como te llamas?' en ingles?", "respuesta_correcta": "what is your name",
             "alternativas": ["what is your name", "whats your name"], "pista": "what = que, your = tu."},
            {"pregunta": "Que significa 'Nice to meet you'?", "respuesta_correcta": "mucho gusto",
             "alternativas": ["mucho gusto", "encantado"], "pista": "Se dice al conocer a alguien."},
        ],
    },
    {
        "id": "A1-03", "nivel": "A1", "nombre": "Numeros del 1 al 10",
        "objetivo": "Contar y decir numeros basicos en ingles",
        "vocabulario": [
            {"ingles": "One", "pronunciacion": "uan", "espanol": "Uno"},
            {"ingles": "Two", "pronunciacion": "tu", "espanol": "Dos"},
            {"ingles": "Three", "pronunciacion": "zri", "espanol": "Tres"},
            {"ingles": "Four", "pronunciacion": "for", "espanol": "Cuatro"},
            {"ingles": "Five", "pronunciacion": "faiv", "espanol": "Cinco"},
            {"ingles": "Six", "pronunciacion": "siks", "espanol": "Seis"},
            {"ingles": "Seven", "pronunciacion": "se-ven", "espanol": "Siete"},
            {"ingles": "Eight", "pronunciacion": "eit", "espanol": "Ocho"},
            {"ingles": "Nine", "pronunciacion": "nain", "espanol": "Nueve"},
            {"ingles": "Ten", "pronunciacion": "ten", "espanol": "Diez"},
        ],
        "preguntas": [
            {"pregunta": "Como se dice 'cinco' en ingles?", "respuesta_correcta": "five",
             "alternativas": ["five", "faiv"], "pista": "Empieza con F."},
            {"pregunta": "Que significa 'seven'?", "respuesta_correcta": "siete",
             "alternativas": ["siete"], "pista": "Esta entre el 6 y el 8."},
            {"pregunta": "Como se escribe el numero 3 en ingles?", "respuesta_correcta": "three",
             "alternativas": ["three"], "pista": "Lleva 'ee' al final."},
        ],
    },
    {
        "id": "A1-04", "nivel": "A1", "nombre": "Colores",
        "objetivo": "Nombrar los colores basicos",
        "vocabulario": [
            {"ingles": "Red", "pronunciacion": "red", "espanol": "Rojo"},
            {"ingles": "Blue", "pronunciacion": "blu", "espanol": "Azul"},
            {"ingles": "Green", "pronunciacion": "grin", "espanol": "Verde"},
            {"ingles": "Yellow", "pronunciacion": "ie-lou", "espanol": "Amarillo"},
            {"ingles": "Black", "pronunciacion": "blak", "espanol": "Negro"},
            {"ingles": "White", "pronunciacion": "uait", "espanol": "Blanco"},
            {"ingles": "Orange", "pronunciacion": "o-rinch", "espanol": "Naranja"},
            {"ingles": "Pink", "pronunciacion": "pink", "espanol": "Rosa"},
        ],
        "preguntas": [
            {"pregunta": "Como se dice 'azul' en ingles?", "respuesta_correcta": "blue",
             "alternativas": ["blue"], "pista": "Es el color del cielo."},
            {"pregunta": "Que significa 'white'?", "respuesta_correcta": "blanco",
             "alternativas": ["blanco"], "pista": "Es el color de la nieve."},
            {"pregunta": "Como se dice 'verde' en ingles?", "respuesta_correcta": "green",
             "alternativas": ["green"], "pista": "Es el color de las plantas."},
        ],
    },
    {
        "id": "A1-05", "nivel": "A1", "nombre": "Dias de la semana",
        "objetivo": "Aprender los dias de la semana",
        "vocabulario": [
            {"ingles": "Monday", "pronunciacion": "man-dei", "espanol": "Lunes"},
            {"ingles": "Tuesday", "pronunciacion": "tius-dei", "espanol": "Martes"},
            {"ingles": "Wednesday", "pronunciacion": "uens-dei", "espanol": "Miercoles"},
            {"ingles": "Thursday", "pronunciacion": "zers-dei", "espanol": "Jueves"},
            {"ingles": "Friday", "pronunciacion": "frai-dei", "espanol": "Viernes"},
            {"ingles": "Saturday", "pronunciacion": "sa-ter-dei", "espanol": "Sabado"},
            {"ingles": "Sunday", "pronunciacion": "san-dei", "espanol": "Domingo"},
        ],
        "preguntas": [
            {"pregunta": "Como se dice 'lunes' en ingles?", "respuesta_correcta": "monday",
             "alternativas": ["monday"], "pista": "Empieza con M, significa 'dia de la luna'."},
            {"pregunta": "Que dia es 'Friday'?", "respuesta_correcta": "viernes",
             "alternativas": ["viernes"], "pista": "Es el quinto dia de la semana."},
            {"pregunta": "Como se dice 'domingo' en ingles?", "respuesta_correcta": "sunday",
             "alternativas": ["sunday"], "pista": "Empieza con S."},
        ],
    },
    {
        "id": "A1-06", "nivel": "A1", "nombre": "Verbo To Be (ser/estar)",
        "objetivo": "Usar el verbo to be en presente",
        "vocabulario": [
            {"ingles": "I am", "pronunciacion": "ai am", "espanol": "Yo soy/estoy"},
            {"ingles": "You are", "pronunciacion": "iu ar", "espanol": "Tu eres/estas"},
            {"ingles": "He is", "pronunciacion": "ji is", "espanol": "El es/esta"},
            {"ingles": "She is", "pronunciacion": "shi is", "espanol": "Ella es/esta"},
            {"ingles": "It is", "pronunciacion": "it is", "espanol": "Eso es/esta"},
            {"ingles": "We are", "pronunciacion": "ui ar", "espanol": "Nosotros somos/estamos"},
            {"ingles": "They are", "pronunciacion": "zei ar", "espanol": "Ellos son/estan"},
        ],
        "preguntas": [
            {"pregunta": "Como se dice 'Yo soy' en ingles?", "respuesta_correcta": "i am",
             "alternativas": ["i am", "im"], "pista": "I = yo, am = soy."},
            {"pregunta": "Completa: She ___ a teacher", "respuesta_correcta": "is",
             "alternativas": ["is"], "pista": "She + verbo en tercera persona."},
            {"pregunta": "Como se dice 'Ellos son' en ingles?", "respuesta_correcta": "they are",
             "alternativas": ["they are", "theyre"], "pista": "They = ellos, are = son."},
        ],
    },
    {
        "id": "A1-07", "nivel": "A1", "nombre": "La familia",
        "objetivo": "Nombrar a los miembros de la familia",
        "vocabulario": [
            {"ingles": "Mother", "pronunciacion": "mo-zer", "espanol": "Madre"},
            {"ingles": "Father", "pronunciacion": "fa-zer", "espanol": "Padre"},
            {"ingles": "Brother", "pronunciacion": "bro-zer", "espanol": "Hermano"},
            {"ingles": "Sister", "pronunciacion": "sis-ter", "espanol": "Hermana"},
            {"ingles": "Son", "pronunciacion": "son", "espanol": "Hijo"},
            {"ingles": "Daughter", "pronunciacion": "do-ter", "espanol": "Hija"},
            {"ingles": "Family", "pronunciacion": "fa-mi-li", "espanol": "Familia"},
        ],
        "preguntas": [
            {"pregunta": "Como se dice 'madre' en ingles?", "respuesta_correcta": "mother",
             "alternativas": ["mother", "mom"], "pista": "Tambien se dice 'mom' informalmente."},
            {"pregunta": "Que significa 'brother'?", "respuesta_correcta": "hermano",
             "alternativas": ["hermano"], "pista": "Es un varon de la familia."},
            {"pregunta": "Como se dice 'hija' en ingles?", "respuesta_correcta": "daughter",
             "alternativas": ["daughter"], "pista": "Se pronuncia 'do-ter'."},
        ],
    },
    {
        "id": "A1-08", "nivel": "A1", "nombre": "Comida y bebida basica",
        "objetivo": "Pedir comida y bebida basica",
        "vocabulario": [
            {"ingles": "Water", "pronunciacion": "uo-ter", "espanol": "Agua"},
            {"ingles": "Coffee", "pronunciacion": "co-fi", "espanol": "Cafe"},
            {"ingles": "Tea", "pronunciacion": "ti", "espanol": "Te"},
            {"ingles": "Bread", "pronunciacion": "bred", "espanol": "Pan"},
            {"ingles": "Rice", "pronunciacion": "rais", "espanol": "Arroz"},
            {"ingles": "Chicken", "pronunciacion": "chi-ken", "espanol": "Pollo"},
            {"ingles": "Apple", "pronunciacion": "a-pol", "espanol": "Manzana"},
        ],
        "preguntas": [
            {"pregunta": "Como se dice 'agua' en ingles?", "respuesta_correcta": "water",
             "alternativas": ["water"], "pista": "Empieza con W."},
            {"pregunta": "Que significa 'coffee'?", "respuesta_correcta": "cafe",
             "alternativas": ["cafe"], "pista": "Bebida caliente muy popular."},
            {"pregunta": "Como se dice 'manzana' en ingles?", "respuesta_correcta": "apple",
             "alternativas": ["apple"], "pista": "Fruta roja o verde."},
        ],
    },
    {
        "id": "A1-09", "nivel": "A1", "nombre": "Preguntas basicas con Wh-",
        "objetivo": "Formular preguntas simples con What, Where, When, Who",
        "vocabulario": [
            {"ingles": "What", "pronunciacion": "uot", "espanol": "Que / Cual"},
            {"ingles": "Where", "pronunciacion": "uer", "espanol": "Donde"},
            {"ingles": "When", "pronunciacion": "uen", "espanol": "Cuando"},
            {"ingles": "Who", "pronunciacion": "ju", "espanol": "Quien"},
            {"ingles": "How", "pronunciacion": "jau", "espanol": "Como"},
            {"ingles": "Why", "pronunciacion": "uai", "espanol": "Por que"},
        ],
        "preguntas": [
            {"pregunta": "Que palabra se usa para preguntar 'donde'?", "respuesta_correcta": "where",
             "alternativas": ["where"], "pista": "Empieza con W."},
            {"pregunta": "Como preguntas 'quien' en ingles?", "respuesta_correcta": "who",
             "alternativas": ["who"], "pista": "Es una palabra de 3 letras."},
            {"pregunta": "Que significa 'when'?", "respuesta_correcta": "cuando",
             "alternativas": ["cuando"], "pista": "Pregunta sobre tiempo."},
        ],
    },
    {
        "id": "A1-10", "nivel": "A1", "nombre": "Frases de supervivencia",
        "objetivo": "Frases utiles para el dia a dia",
        "vocabulario": [
            {"ingles": "How much is it?", "pronunciacion": "jau mach is it", "espanol": "Cuanto cuesta?"},
            {"ingles": "Where is the bathroom?", "pronunciacion": "uer is de baz-rum", "espanol": "Donde esta el bano?"},
            {"ingles": "I don't understand", "pronunciacion": "ai dont an-der-stand", "espanol": "No entiendo"},
            {"ingles": "Can you repeat please?", "pronunciacion": "kan iu ri-pit plis", "espanol": "Puede repetir?"},
            {"ingles": "Excuse me", "pronunciacion": "ex-kius mi", "espanol": "Disculpe"},
            {"ingles": "Help me", "pronunciacion": "jelp mi", "espanol": "Ayudame"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'No entiendo' en ingles?", "respuesta_correcta": "i dont understand",
             "alternativas": ["i dont understand", "i do not understand"], "pista": "dont = do not."},
            {"pregunta": "Como preguntas 'Cuanto cuesta?' en ingles?", "respuesta_correcta": "how much is it",
             "alternativas": ["how much is it"], "pista": "How = como, much = mucho."},
            {"pregunta": "Que significa 'excuse me'?", "respuesta_correcta": "disculpe",
             "alternativas": ["disculpe", "perdon"], "pista": "Se usa para llamar la atencion."},
        ],
    },
]

# ============================================================
# NIVEL A2 - Elemental (Plataforma)
# ============================================================
TEMARIO_A2 = [
    {
        "id": "A2-01", "nivel": "A2", "nombre": "Rutina diaria",
        "objetivo": "Describir tus actividades cotidianas",
        "vocabulario": [
            {"ingles": "I wake up", "pronunciacion": "ai ueik ap", "espanol": "Me despierto"},
            {"ingles": "I get up", "pronunciacion": "ai get ap", "espanol": "Me levanto"},
            {"ingles": "I have breakfast", "pronunciacion": "ai jav brek-fast", "espanol": "Desayuno"},
            {"ingles": "I go to work", "pronunciacion": "ai gou tu uork", "espanol": "Voy a trabajar"},
            {"ingles": "I have lunch", "pronunciacion": "ai jav lanch", "espanol": "Almuerzo"},
            {"ingles": "I come back home", "pronunciacion": "ai kam bak jom", "espanol": "Regreso a casa"},
            {"ingles": "I go to sleep", "pronunciacion": "ai gou tu slip", "espanol": "Me voy a dormir"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'Me despierto' en ingles?", "respuesta_correcta": "i wake up",
             "alternativas": ["i wake up"], "pista": "Wake = despertar, up = arriba."},
            {"pregunta": "Completa: I ___ breakfast at 7am", "respuesta_correcta": "have",
             "alternativas": ["have"], "pista": "Verbo tener/tomar."},
            {"pregunta": "Como dices 'Voy a trabajar' en ingles?", "respuesta_correcta": "i go to work",
             "alternativas": ["i go to work"], "pista": "go = ir, work = trabajar."},
        ],
    },
    {
        "id": "A2-02", "nivel": "A2", "nombre": "Pasado simple (verbo to be)",
        "objetivo": "Hablar de cosas que pasaron ayer o antes",
        "vocabulario": [
            {"ingles": "I was", "pronunciacion": "ai uos", "espanol": "Yo era/estuve (pasado)"},
            {"ingles": "You were", "pronunciacion": "iuer", "espanol": "Tu eras/estuviste"},
            {"ingles": "He was", "pronunciacion": "ji uos", "espanol": "El era/estuvo"},
            {"ingles": "She was", "pronunciacion": "shi uos", "espanol": "Ella era/estuvo"},
            {"ingles": "It was", "pronunciacion": "it uos", "espanol": "Eso era/estuvo"},
            {"ingles": "We were", "pronunciacion": "ui uer", "espanol": "Nosotros eramos/estuvimos"},
            {"ingles": "They were", "pronunciacion": "zei uer", "espanol": "Ellos eran/estuvieron"},
        ],
        "preguntas": [
            {"pregunta": "Completa en pasado: She ___ happy yesterday", "respuesta_correcta": "was",
             "alternativas": ["was"], "pista": "Pasado de 'is' para she/he/it."},
            {"pregunta": "Como dices 'Yo estuve' en pasado?", "respuesta_correcta": "i was",
             "alternativas": ["i was"], "pista": "Pasado de I am."},
            {"pregunta": "Completa: They ___ at home last night", "respuesta_correcta": "were",
             "alternativas": ["were"], "pista": "Plural en pasado."},
        ],
    },
    {
        "id": "A2-03", "nivel": "A2", "nombre": "Pasado simple (verbos regulares)",
        "objetivo": "Contar lo que hiciste en el pasado",
        "vocabulario": [
            {"ingles": "I worked", "pronunciacion": "ai uorkt", "espanol": "Yo trabaje"},
            {"ingles": "I studied", "pronunciacion": "ai sta-did", "espanol": "Yo estudie"},
            {"ingles": "I played", "pronunciacion": "ai pleid", "espanol": "Yo jugue"},
            {"ingles": "I watched", "pronunciacion": "ai uocht", "espanol": "Yo vi/mire"},
            {"ingles": "I cooked", "pronunciacion": "ai kukt", "espanol": "Yo cocine"},
            {"ingles": "I talked", "pronunciacion": "ai tokt", "espanol": "Yo hable"},
            {"ingles": "I walked", "pronunciacion": "ai uokt", "espanol": "Yo camine"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'Yo trabaje' (ayer)?", "respuesta_correcta": "i worked",
             "alternativas": ["i worked"], "pista": "Work + ed = pasado."},
            {"pregunta": "Completa: She ___ English last year", "respuesta_correcta": "studied",
             "alternativas": ["studied"], "pista": "Study cambia la Y por I antes de ED."},
            {"pregunta": "Como dices 'Yo jugue' en pasado?", "respuesta_correcta": "i played",
             "alternativas": ["i played"], "pista": "Play + ed."},
        ],
    },
    {
        "id": "A2-04", "nivel": "A2", "nombre": "Futuro con 'going to'",
        "objetivo": "Hablar de planes futuros",
        "vocabulario": [
            {"ingles": "I am going to...", "pronunciacion": "ai am gouing tu", "espanol": "Yo voy a..."},
            {"ingles": "You are going to...", "pronunciacion": "iu ar gouing tu", "espanol": "Tu vas a..."},
            {"ingles": "He is going to...", "pronunciacion": "ji is gouing tu", "espanol": "El va a..."},
            {"ingles": "What are you going to do?", "pronunciacion": "uot ar iu gouing tu du", "espanol": "Que vas a hacer?"},
            {"ingles": "I am going to travel", "pronunciacion": "ai am gouing tu tra-vel", "espanol": "Voy a viajar"},
        ],
        "preguntas": [
            {"pregunta": "Completa: I ___ going to study tomorrow", "respuesta_correcta": "am",
             "alternativas": ["am"], "pista": "I + verbo to be + going to."},
            {"pregunta": "Como preguntas 'Que vas a hacer?' en ingles?", "respuesta_correcta": "what are you going to do",
             "alternativas": ["what are you going to do"], "pista": "What + are you + going to + do."},
            {"pregunta": "Como dices 'Voy a viajar' en ingles?", "respuesta_correcta": "i am going to travel",
             "alternativas": ["i am going to travel"], "pista": "Travel = viajar."},
        ],
    },
    {
        "id": "A2-05", "nivel": "A2", "nombre": "Modales basicos (can, must, should)",
        "objetivo": "Expresar habilidad, obligacion y consejo",
        "vocabulario": [
            {"ingles": "I can swim", "pronunciacion": "ai kan suim", "espanol": "Yo puedo nadar"},
            {"ingles": "You must study", "pronunciacion": "iu mast sta-di", "espanol": "Debes estudiar"},
            {"ingles": "You should eat", "pronunciacion": "iu shud it", "espanol": "Deberias comer"},
            {"ingles": "I can't drive", "pronunciacion": "ai kant draiv", "espanol": "No puedo conducir"},
            {"ingles": "May I help you?", "pronunciacion": "mei ai jelp iu", "espanol": "Puedo ayudarte?"},
        ],
        "preguntas": [
            {"pregunta": "Que modal se usa para habilidad?", "respuesta_correcta": "can",
             "alternativas": ["can"], "pista": "I ___ swim."},
            {"pregunta": "Completa: You ___ study more (consejo)", "respuesta_correcta": "should",
             "alternativas": ["should"], "pista": "Es un consejo, no obligacion."},
            {"pregunta": "Que significa 'must'?", "respuesta_correcta": "deber",
             "alternativas": ["deber", "tener que"], "pista": "Expresa obligacion."},
        ],
    },
    {
        "id": "A2-06", "nivel": "A2", "nombre": "Comparativos y superlativos",
        "objetivo": "Comparar cosas y personas",
        "vocabulario": [
            {"ingles": "Bigger than", "pronunciacion": "bi-ger zan", "espanol": "Mas grande que"},
            {"ingles": "Smaller than", "pronunciacion": "smol-ler zan", "espanol": "Mas pequeno que"},
            {"ingles": "The biggest", "pronunciacion": "de bi-gest", "espanol": "El mas grande"},
            {"ingles": "More expensive than", "pronunciacion": "mor ex-pen-siv zan", "espanol": "Mas caro que"},
            {"ingles": "The most beautiful", "pronunciacion": "de most biu-ti-ful", "espanol": "El/la mas hermoso/a"},
            {"ingles": "Better than", "pronunciacion": "be-ter zan", "espanol": "Mejor que"},
        ],
        "preguntas": [
            {"pregunta": "Completa: This book is ___ than that one (grande)", "respuesta_correcta": "bigger",
             "alternativas": ["bigger"], "pista": "Big + ger + than."},
            {"pregunta": "Como dices 'el mas grande' (superlativo)?", "respuesta_correcta": "the biggest",
             "alternativas": ["the biggest"], "pista": "The + big + gest."},
            {"pregunta": "Completa: She is ___ than her sister (rapida)", "respuesta_correcta": "faster",
             "alternativas": ["faster"], "pista": "Fast + er + than."},
        ],
    },
    {
        "id": "A2-07", "nivel": "A2", "nombre": "Ir de compras",
        "objetivo": "Comprender y usar vocabulario de compras",
        "vocabulario": [
            {"ingles": "How much does it cost?", "pronunciacion": "jau mach das it kost", "espanol": "Cuanto cuesta?"},
            {"ingles": "Can I try it on?", "pronunciacion": "kan ai trai it on", "espanol": "Puedo probarmelo?"},
            {"ingles": "Do you have a smaller size?", "pronunciacion": "du iu jav a smol-ler sais", "espanol": "Tiene una talla mas pequena?"},
            {"ingles": "I'll take it", "pronunciacion": "ail teik it", "espanol": "Me lo llevo"},
            {"ingles": "Too expensive", "pronunciacion": "tu ex-pen-siv", "espanol": "Demasiado caro"},
            {"ingles": "The fitting room", "pronunciacion": "de fi-ting rum", "espanol": "El probador"},
        ],
        "preguntas": [
            {"pregunta": "Como pides probarte algo?", "respuesta_correcta": "can i try it on",
             "alternativas": ["can i try it on"], "pista": "Try = probar, on = puesto."},
            {"pregunta": "Que significa 'too expensive'?", "respuesta_correcta": "muy caro",
             "alternativas": ["muy caro", "demasiado caro"], "pista": "Too = demasiado."},
            {"pregunta": "Como dices 'Me lo llevo'?", "respuesta_correcta": "ill take it",
             "alternativas": ["ill take it", "i will take it"], "pista": "I'll = I will."},
        ],
    },
    {
        "id": "A2-08", "nivel": "A2", "nombre": "La salud y el cuerpo",
        "objetivo": "Hablar sobre tu salud y sintomas",
        "vocabulario": [
            {"ingles": "I have a headache", "pronunciacion": "ai jav a je-deik", "espanol": "Tengo dolor de cabeza"},
            {"ingles": "I have a cold", "pronunciacion": "ai jav a cold", "espanol": "Estoy resfriado"},
            {"ingles": "I have a fever", "pronunciacion": "ai jav a fi-ver", "espanol": "Tengo fiebre"},
            {"ingles": "I need a doctor", "pronunciacion": "ai nid a doc-tor", "espanol": "Necesito un medico"},
            {"ingles": "My stomach hurts", "pronunciacion": "mai sto-mak jerts", "espanol": "Me duele el estomago"},
            {"ingles": "I feel better", "pronunciacion": "ai fil be-ter", "espanol": "Me siento mejor"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'Tengo dolor de cabeza'?", "respuesta_correcta": "i have a headache",
             "alternativas": ["i have a headache"], "pista": "Head = cabeza, ache = dolor."},
            {"pregunta": "Que significa 'I have a fever'?", "respuesta_correcta": "tengo fiebre",
             "alternativas": ["tengo fiebre"], "pista": "Fever = fiebre."},
            {"pregunta": "Como dices 'Necesito un medico'?", "respuesta_correcta": "i need a doctor",
             "alternativas": ["i need a doctor"], "pista": "Need = necesitar."},
        ],
    },
    {
        "id": "A2-09", "nivel": "A2", "nombre": "Medios de transporte",
        "objetivo": "Hablar sobre como te mueves por la ciudad",
        "vocabulario": [
            {"ingles": "By car", "pronunciacion": "bai kar", "espanol": "En carro"},
            {"ingles": "By bus", "pronunciacion": "bai bas", "espanol": "En bus"},
            {"ingles": "By train", "pronunciacion": "bai trein", "espanol": "En tren"},
            {"ingles": "By plane", "pronunciacion": "bai plein", "espanol": "En avion"},
            {"ingles": "By bike", "pronunciacion": "bai baik", "espanol": "En bicicleta"},
            {"ingles": "On foot", "pronunciacion": "on fut", "espanol": "A pie"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'en bus' en ingles?", "respuesta_correcta": "by bus",
             "alternativas": ["by bus"], "pista": "By = en/por, bus = autobus."},
            {"pregunta": "Que significa 'on foot'?", "respuesta_correcta": "a pie",
             "alternativas": ["a pie", "caminando"], "pista": "Foot = pie."},
            {"pregunta": "Como dices 'en bicicleta'?", "respuesta_correcta": "by bike",
             "alternativas": ["by bike"], "pista": "Bike = bicicleta."},
        ],
    },
    {
        "id": "A2-10", "nivel": "A2", "nombre": "Tiempo y clima",
        "objetivo": "Describir el clima y las estaciones",
        "vocabulario": [
            {"ingles": "It's sunny", "pronunciacion": "its sa-ni", "espanol": "Esta soleado"},
            {"ingles": "It's rainy", "pronunciacion": "its rei-ni", "espanol": "Esta lluvioso"},
            {"ingles": "It's cold", "pronunciacion": "its cold", "espanol": "Hace frio"},
            {"ingles": "It's hot", "pronunciacion": "its jot", "espanol": "Hace calor"},
            {"ingles": "It's cloudy", "pronunciacion": "its klau-di", "espanol": "Esta nublado"},
            {"ingles": "It's snowing", "pronunciacion": "its snou-ing", "espanol": "Esta nevando"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'Hace calor'?", "respuesta_correcta": "its hot",
             "alternativas": ["its hot"], "pista": "Hot = caliente."},
            {"pregunta": "Que significa 'it's rainy'?", "respuesta_correcta": "esta lloviendo",
             "alternativas": ["esta lloviendo", "esta lluvioso"], "pista": "Rain = lluvia."},
            {"pregunta": "Como dices 'Esta soleado'?", "respuesta_correcta": "its sunny",
             "alternativas": ["its sunny"], "pista": "Sun = sol."},
        ],
    },
]

# ============================================================
# NIVEL B1 - Intermedio (Umbral)
# ============================================================
TEMARIO_B1 = [
    {
        "id": "B1-01", "nivel": "B1", "nombre": "Presente perfecto basico",
        "objetivo": "Hablar de experiencias pasadas con relevancia presente",
        "vocabulario": [
            {"ingles": "I have been to...", "pronunciacion": "ai jav bin tu", "espanol": "He estado en..."},
            {"ingles": "I have never...", "pronunciacion": "ai jav ne-ver", "espanol": "Nunca he..."},
            {"ingles": "I have already...", "pronunciacion": "ai jav ol-re-di", "espanol": "Ya he..."},
            {"ingles": "I have just...", "pronunciacion": "ai jav yost", "espanol": "Acabo de..."},
            {"ingles": "Have you ever...?", "pronunciacion": "jav iu e-ver", "espanol": "Alguna vez has...?"},
            {"ingles": "I haven't...", "pronunciacion": "ai jav-ent", "espanol": "No he..."},
        ],
        "preguntas": [
            {"pregunta": "Completa: I ___ never been to Japan", "respuesta_correcta": "have",
             "alternativas": ["have"], "pista": "I + have + never."},
            {"pregunta": "Como preguntas 'Alguna vez has...?'", "respuesta_correcta": "have you ever",
             "alternativas": ["have you ever"], "pista": "Have + you + ever."},
            {"pregunta": "Que significa 'I have just arrived'?", "respuesta_correcta": "acabo de llegar",
             "alternativas": ["acabo de llegar"], "pista": "Just = hace poco."},
        ],
    },
    {
        "id": "B1-02", "nivel": "B1", "nombre": "Expresar opiniones",
        "objetivo": "Dar tu opinion sobre temas diversos",
        "vocabulario": [
            {"ingles": "I think that...", "pronunciacion": "ai zink zat", "espanol": "Yo creo que..."},
            {"ingles": "In my opinion...", "pronunciacion": "in mai o-pi-nion", "espanol": "En mi opinion..."},
            {"ingles": "I agree with you", "pronunciacion": "ai a-gri uiz iu", "espanol": "Estoy de acuerdo contigo"},
            {"ingles": "I disagree", "pronunciacion": "ai dis-a-gri", "espanol": "No estoy de acuerdo"},
            {"ingles": "That's a good point", "pronunciacion": "zats a gud point", "espanol": "Es un buen punto"},
            {"ingles": "I'm not sure", "pronunciacion": "aim not shur", "espanol": "No estoy seguro"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'Yo creo que'?", "respuesta_correcta": "i think that",
             "alternativas": ["i think that", "i think"], "pista": "Think = pensar/creer."},
            {"pregunta": "Que significa 'I agree'?", "respuesta_correcta": "estoy de acuerdo",
             "alternativas": ["estoy de acuerdo", "coincido"], "pista": "Agree = estar de acuerdo."},
            {"pregunta": "Como dices 'No estoy seguro'?", "respuesta_correcta": "im not sure",
             "alternativas": ["im not sure", "i am not sure"], "pista": "Sure = seguro."},
        ],
    },
    {
        "id": "B1-03", "nivel": "B1", "nombre": "Vocabulario de trabajo",
        "objetivo": "Hablar sobre tu trabajo y profesion",
        "vocabulario": [
            {"ingles": "I work as a...", "pronunciacion": "ai uork as a", "espanol": "Trabajo como..."},
            {"ingles": "My boss is...", "pronunciacion": "mai bos is", "espanol": "Mi jefe es..."},
            {"ingles": "I have a meeting", "pronunciacion": "ai jav a mi-ting", "espanol": "Tengo una reunion"},
            {"ingles": "The deadline is...", "pronunciacion": "de ded-lain is", "espanol": "La fecha limite es..."},
            {"ingles": "I earn...", "pronunciacion": "ai ern", "espanol": "Gano..."},
            {"ingles": "I'm looking for a job", "pronunciacion": "aim lu-king for a yob", "espanol": "Estoy buscando trabajo"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'Tengo una reunion'?", "respuesta_correcta": "i have a meeting",
             "alternativas": ["i have a meeting"], "pista": "Meeting = reunion."},
            {"pregunta": "Que significa 'deadline'?", "respuesta_correcta": "fecha limite",
             "alternativas": ["fecha limite", "plazo"], "pista": "Linea final de tiempo."},
            {"pregunta": "Como dices 'Estoy buscando trabajo'?", "respuesta_correcta": "im looking for a job",
             "alternativas": ["im looking for a job"], "pista": "Looking for = buscando."},
        ],
    },
    {
        "id": "B1-04", "nivel": "B1", "nombre": "Conectores logicos",
        "objetivo": "Unir ideas y dar razones",
        "vocabulario": [
            {"ingles": "And", "pronunciacion": "and", "espanol": "Y"},
            {"ingles": "But", "pronunciacion": "bat", "espanol": "Pero"},
            {"ingles": "Because", "pronunciacion": "bi-kos", "espanol": "Porque"},
            {"ingles": "So", "pronunciacion": "sou", "espanol": "Entonces"},
            {"ingles": "Although", "pronunciacion": "ol-DOU", "espanol": "Aunque"},
            {"ingles": "However", "pronunciacion": "jau-e-ver", "espanol": "Sin embargo"},
        ],
        "preguntas": [
            {"pregunta": "Que conector significa 'porque'?", "respuesta_correcta": "because",
             "alternativas": ["because"], "pista": "Da una razon o causa."},
            {"pregunta": "Completa: I like coffee, ___ I don't like tea", "respuesta_correcta": "but",
             "alternativas": ["but"], "pista": "Expresa contraste."},
            {"pregunta": "Que significa 'although'?", "respuesta_correcta": "aunque",
             "alternativas": ["aunque"], "pista": "Expresa una concesion."},
        ],
    },
    {
        "id": "B1-05", "nivel": "B1", "nombre": "Vocabulario de viajes",
        "objetivo": "Hablar sobre experiencias de viaje",
        "vocabulario": [
            {"ingles": "I would like to book...", "pronunciacion": "ai wuod laik tu buk", "espanol": "Quisiera reservar..."},
            {"ingles": "A single room", "pronunciacion": "a sin-guel rum", "espanol": "Habitacion individual"},
            {"ingles": "A double room", "pronunciacion": "a do-bol rum", "espanol": "Habitacion doble"},
            {"ingles": "Check-in", "pronunciacion": "chek-in", "espanol": "Registrarse (en hotel)"},
            {"ingles": "Check-out", "pronunciacion": "chek-aut", "espanol": "Salir (del hotel)"},
            {"ingles": "Luggage", "pronunciacion": "la-guech", "espanol": "Equipaje"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'Quisiera reservar' en ingles?", "respuesta_correcta": "i would like to book",
             "alternativas": ["i would like to book", "id like to book"], "pista": "I would like = quisiera."},
            {"pregunta": "Que significa 'check-in'?", "respuesta_correcta": "registrarse",
             "alternativas": ["registrarse", "registro de entrada"], "pista": "Es al llegar a un hotel."},
            {"pregunta": "Como dices 'equipaje' en ingles?", "respuesta_correcta": "luggage",
             "alternativas": ["luggage"], "pista": "Es lo que llevas en tus viajes."},
        ],
    },
    {
        "id": "B1-06", "nivel": "B1", "nombre": "Condicionales tipo 1 y 2",
        "objetivo": "Hablar de situaciones reales e hipoteticas",
        "vocabulario": [
            {"ingles": "If it rains, I will stay home", "pronunciacion": "if it reins ai uil stei jom", "espanol": "Si llueve, me quedare en casa"},
            {"ingles": "If I had money, I would travel", "pronunciacion": "if ai jav mo-ni ai wuod tra-vel", "espanol": "Si tuviera dinero, viajaria"},
            {"ingles": "If you study, you will pass", "pronunciacion": "if iu sta-di iu uil pas", "espanol": "Si estudias, aprobaras"},
            {"ingles": "If I were you, I would go", "pronunciacion": "if ai uer iu ai wuod gou", "espanol": "Si yo fuera tu, iria"},
        ],
        "preguntas": [
            {"pregunta": "Completa: If it rains, I ___ stay home", "respuesta_correcta": "will",
             "alternativas": ["will"], "pista": "Primer condicional: if + presente, will + verbo."},
            {"pregunta": "Como dices 'Si tuviera dinero, viajaria'?", "respuesta_correcta": "if i had money i would travel",
             "alternativas": ["if i had money i would travel"], "pista": "Segundo condicional."},
        ],
    },
    {
        "id": "B1-07", "nivel": "B1", "nombre": "Pronombres reflexivos",
        "objetivo": "Usar pronombres reflexivos correctamente",
        "vocabulario": [
            {"ingles": "Myself", "pronunciacion": "mai-self", "espanol": "Yo mismo"},
            {"ingles": "Yourself", "pronunciacion": "ior-self", "espanol": "Tu mismo"},
            {"ingles": "Himself", "pronunciacion": "jim-self", "espanol": "El mismo"},
            {"ingles": "Herself", "pronunciacion": "jer-self", "espanol": "Ella misma"},
            {"ingles": "Ourselves", "pronunciacion": "aur-selvz", "espanol": "Nosotros mismos"},
            {"ingles": "Themselves", "pronunciacion": "zem-selvz", "espanol": "Ellos mismos"},
        ],
        "preguntas": [
            {"pregunta": "Que pronombre reflexivo corresponde a 'he'?", "respuesta_correcta": "himself",
             "alternativas": ["himself"], "pista": "He + self."},
            {"pregunta": "Completa: I can do it ___ (yo mismo)", "respuesta_correcta": "myself",
             "alternativas": ["myself"], "pista": "I + self."},
            {"pregunta": "Como dices 'ellos mismos'?", "respuesta_correcta": "themselves",
             "alternativas": ["themselves"], "pista": "They + selves."},
        ],
    },
    {
        "id": "B1-08", "nivel": "B1", "nombre": "Vocabulario de tecnologia",
        "objetivo": "Hablar sobre tecnologia y redes sociales",
        "vocabulario": [
            {"ingles": "Social media", "pronunciacion": "sou-shal mi-dia", "espanol": "Redes sociales"},
            {"ingles": "To download", "pronunciacion": "tu dau-load", "espanol": "Descargar"},
            {"ingles": "To upload", "pronunciacion": "tu ap-load", "espanol": "Subir (archivos)"},
            {"ingles": "Password", "pronunciacion": "pas-uerd", "espanol": "Contrasena"},
            {"ingles": "Wi-Fi connection", "pronunciacion": "uai-fai con-nec-shon", "espanol": "Conexion Wi-Fi"},
            {"ingles": "To charge (phone)", "pronunciacion": "tu chary", "espanol": "Cargar (el telefono)"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'descargar' en ingles?", "respuesta_correcta": "to download",
             "alternativas": ["to download", "download"], "pista": "Down = abajo, load = cargar."},
            {"pregunta": "Que significa 'password'?", "respuesta_correcta": "contrasena",
             "alternativas": ["contrasena", "clave"], "pista": "La usas para entrar a cuentas."},
            {"pregunta": "Como dices 'redes sociales'?", "respuesta_correcta": "social media",
             "alternativas": ["social media"], "pista": "Social = social, media = medios."},
        ],
    },
    {
        "id": "B1-09", "nivel": "B1", "nombre": "Reported speech basico",
        "objetivo": "Contar lo que alguien dijo",
        "vocabulario": [
            {"ingles": "He said that...", "pronunciacion": "ji sed zat", "espanol": "El dijo que..."},
            {"ingles": "She told me that...", "pronunciacion": "shi told mi zat", "espanol": "Ella me dijo que..."},
            {"ingles": "He said he was tired", "pronunciacion": "ji sed ji uos tai-erd", "espanol": "El dijo que estaba cansado"},
            {"ingles": "They said they would come", "pronunciacion": "zei sed zei wuod com", "espanol": "Dijeron que vendrian"},
        ],
        "preguntas": [
            {"pregunta": "Como reportas 'I am happy'?", "respuesta_correcta": "he said he was happy",
             "alternativas": ["he said he was happy"], "pista": "El presente cambia a pasado."},
            {"pregunta": "Que significa 'she told me'?", "respuesta_correcta": "ella me dijo",
             "alternativas": ["ella me dijo"], "pista": "Tell = contar/decir."},
        ],
    },
    {
        "id": "B1-10", "nivel": "B1", "nombre": "Vocabulario de emociones",
        "objetivo": "Expresar emociones y estados de animo",
        "vocabulario": [
            {"ingles": "I feel anxious", "pronunciacion": "ai fil ank-shos", "espanol": "Me siento ansioso"},
            {"ingles": "I'm stressed out", "pronunciacion": "aim stressed aut", "espanol": "Estoy estresado"},
            {"ingles": "I'm excited about", "pronunciacion": "aim ex-sai-ted a-baut", "espanol": "Estoy emocionado por"},
            {"ingles": "I'm fed up with", "pronunciacion": "aim fed up uiz", "espanol": "Estoy harto de"},
            {"ingles": "I'm proud of", "pronunciacion": "aim praud of", "espanol": "Estoy orgulloso de"},
            {"ingles": "I miss you", "pronunciacion": "ai mis iu", "espanol": "Te extrano"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'Estoy estresado'?", "respuesta_correcta": "im stressed out",
             "alternativas": ["im stressed out", "im stressed"], "pista": "Stress = estres."},
            {"pregunta": "Que significa 'I'm proud of you'?", "respuesta_correcta": "estoy orgulloso de ti",
             "alternativas": ["estoy orgulloso de ti"], "pista": "Proud = orgulloso."},
            {"pregunta": "Como dices 'te extrano'?", "respuesta_correcta": "i miss you",
             "alternativas": ["i miss you"], "pista": "Miss = extranar."},
        ],
    },
]

# ============================================================
# NIVEL B2 - Intermedio alto (Ventaja)
# ============================================================
TEMARIO_B2 = [
    {
        "id": "B2-01", "nivel": "B2", "nombre": "Vocabulario avanzado de negocios",
        "objetivo": "Comunicarte en un entorno profesional",
        "vocabulario": [
            {"ingles": "Stakeholder", "pronunciacion": "steik-jol-der", "espanol": "Parte interesada"},
            {"ingles": "Deadline", "pronunciacion": "ded-lain", "espanol": "Fecha limite"},
            {"ingles": "To negotiate", "pronunciacion": "tu ne-go-shi-eit", "espanol": "Negociar"},
            {"ingles": "To delegate", "pronunciacion": "tu de-le-gueit", "espanol": "Delegar"},
            {"ingles": "ROI", "pronunciacion": "ar-o-ai", "espanol": "Retorno de inversion"},
            {"ingles": "To launch a product", "pronunciacion": "tu lonch a pro-duct", "espanol": "Lanzar un producto"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'stakeholder'?", "respuesta_correcta": "parte interesada",
             "alternativas": ["parte interesada", "accionista"], "pista": "Persona interesada en un proyecto."},
            {"pregunta": "Como dices 'negociar' en ingles?", "respuesta_correcta": "to negotiate",
             "alternativas": ["to negotiate", "negotiate"], "pista": "Negociar acuerdos."},
        ],
    },
    {
        "id": "B2-02", "nivel": "B2", "nombre": "Expresiones idiomaticas comunes",
        "objetivo": "Usar modismos en conversaciones naturales",
        "vocabulario": [
            {"ingles": "Break a leg", "pronunciacion": "breik a leg", "espanol": "Buena suerte"},
            {"ingles": "Piece of cake", "pronunciacion": "pis of keik", "espanol": "Pan comido"},
            {"ingles": "Hit the books", "pronunciacion": "jit de buks", "espanol": "Estudiar mucho"},
            {"ingles": "Under the weather", "pronunciacion": "an-der de ue-zer", "espanol": "Estar enfermo"},
            {"ingles": "Spill the beans", "pronunciacion": "spil de bins", "espanol": "Revelar un secreto"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'piece of cake'?", "respuesta_correcta": "pan comido",
             "alternativas": ["pan comido", "facil"], "pista": "Es algo muy facil."},
            {"pregunta": "Como deseas suerte informalmente?", "respuesta_correcta": "break a leg",
             "alternativas": ["break a leg"], "pista": "Expresion teatral."},
        ],
    },
    {
        "id": "B2-03", "nivel": "B2", "nombre": "Discurso formal vs informal",
        "objetivo": "Adaptar tu registro segun el contexto",
        "vocabulario": [
            {"ingles": "I would like to inquire", "pronunciacion": "ai wuod laik tu in-kua-ier", "espanol": "Me gustaria consultar"},
            {"ingles": "Furthermore", "pronunciacion": "fer-zer-mor", "espanol": "Ademas"},
            {"ingles": "Nevertheless", "pronunciacion": "ne-ver-de-les", "espanol": "Sin embargo"},
            {"ingles": "I'm writing to inform you", "pronunciacion": "aim rai-ting tu in-form iu", "espanol": "Le escribo para informarle"},
            {"ingles": "Please do not hesitate to contact me", "pronunciacion": "plis du not jes-ti-teit", "espanol": "Por favor no dude en contactarme"},
        ],
        "preguntas": [
            {"pregunta": "Que conector formal significa 'ademas'?", "respuesta_correcta": "furthermore",
             "alternativas": ["furthermore", "moreover"], "pista": "Ademas de lo anterior."},
            {"pregunta": "Como dices 'No dude en contactarme'?", "respuesta_correcta": "do not hesitate to contact me",
             "alternativas": ["do not hesitate to contact me"], "pista": "Hesitate = dudar."},
        ],
    },
    {
        "id": "B2-04", "nivel": "B2", "nombre": "Condicionales mixtos y avanzados",
        "objetivo": "Hablar de hipotesis complejas",
        "vocabulario": [
            {"ingles": "If I had studied, I would have passed", "pronunciacion": "if ai jav sta-did ai wuod jav past", "espanol": "Si hubiera estudiado, habria aprobado"},
            {"ingles": "If I were the president, I would...", "pronunciacion": "if ai uer de pre-si-dent", "espanol": "Si fuera el presidente, yo..."},
            {"ingles": "I wish I could...", "pronunciacion": "ai uish ai kud", "espanol": "Desearia poder..."},
        ],
        "preguntas": [
            {"pregunta": "Completa: If I had studied, I ___ have passed", "respuesta_correcta": "would",
             "alternativas": ["would"], "pista": "Tercer condicional."},
            {"pregunta": "Como expresas un deseo imposible?", "respuesta_correcta": "i wish i could",
             "alternativas": ["i wish i could", "i wish"], "pista": "Wish = desear."},
        ],
    },
    {
        "id": "B2-05", "nivel": "B2", "nombre": "Discurso indirecto avanzado",
        "objetivo": "Reportar conversaciones complejas",
        "vocabulario": [
            {"ingles": "He asked me if I could help", "pronunciacion": "ji asqt mi if ai kud jelp", "espanol": "Me pregunto si podia ayudar"},
            {"ingles": "She told me to wait", "pronunciacion": "shi told mi tu ueit", "espanol": "Me dijo que esperara"},
            {"ingles": "They wondered whether...", "pronunciacion": "zei uon-dered ue-zer", "espanol": "Se preguntaban si..."},
        ],
        "preguntas": [
            {"pregunta": "Como reportas una pregunta de si/no?", "respuesta_correcta": "he asked me if",
             "alternativas": ["he asked me if", "he asked if"], "pista": "Ask = preguntar."},
        ],
    },
    {
        "id": "B2-06", "nivel": "B2", "nombre": "Phrasal verbs esenciales",
        "objetivo": "Aprender los phrasal verbs mas usados",
        "vocabulario": [
            {"ingles": "Give up", "pronunciacion": "giv ap", "espanol": "Rendirse"},
            {"ingles": "Look forward to", "pronunciacion": "luk for-ward tu", "espanol": "Esperar con ansias"},
            {"ingles": "Put off", "pronunciacion": "put of", "espanol": "Posponer"},
            {"ingles": "Figure out", "pronunciacion": "fi-guer aut", "espanol": "Averiguar"},
            {"ingles": "Get along with", "pronunciacion": "get a-long uiz", "espanol": "Llevarse bien con"},
            {"ingles": "Run out of", "pronunciacion": "ran aut of", "espanol": "Quedarse sin"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'give up'?", "respuesta_correcta": "rendirse",
             "alternativas": ["rendirse", "dejar"], "pista": "Abandonar algo."},
            {"pregunta": "Como dices 'averiguar' como phrasal verb?", "respuesta_correcta": "figure out",
             "alternativas": ["figure out"], "pista": "Figure = figura, out = fuera."},
            {"pregunta": "Que significa 'put off'?", "respuesta_correcta": "posponer",
             "alternativas": ["posponer", "aplazar"], "pista": "Retrasar algo."},
        ],
    },
    {
        "id": "B2-07", "nivel": "B2", "nombre": "Voz pasiva",
        "objetivo": "Usar la voz pasiva en presente y pasado",
        "vocabulario": [
            {"ingles": "It is made in...", "pronunciacion": "it is meid in", "espanol": "Esta hecho en..."},
            {"ingles": "It was written by...", "pronunciacion": "it uos ri-ten bai", "espanol": "Fue escrito por..."},
            {"ingles": "The car was stolen", "pronunciacion": "de car uos stol-en", "espanol": "El carro fue robado"},
            {"ingles": "English is spoken here", "pronunciacion": "in-glish is spou-ken jier", "espanol": "Aqui se habla ingles"},
        ],
        "preguntas": [
            {"pregunta": "Completa: The cake ___ made by my mother", "respuesta_correcta": "was",
             "alternativas": ["was"], "pista": "Pasiva en pasado."},
            {"pregunta": "Como dices 'Aqui se habla ingles'?", "respuesta_correcta": "english is spoken here",
             "alternativas": ["english is spoken here"], "pista": "Voz pasiva: is + participio."},
        ],
    },
    {
        "id": "B2-08", "nivel": "B2", "nombre": "Vocabulario academico",
        "objetivo": "Escribir y hablar en contextos academicos",
        "vocabulario": [
            {"ingles": "To analyze", "pronunciacion": "tu a-na-lais", "espanol": "Analizar"},
            {"ingles": "To conclude", "pronunciacion": "tu con-clu-d", "espanol": "Concluir"},
            {"ingles": "Research", "pronunciacion": "ri-serch", "espanol": "Investigacion"},
            {"ingles": "To argue", "pronunciacion": "tu ar-guiu", "espanol": "Argumentar"},
            {"ingles": "Evidence", "pronunciacion": "e-vi-dens", "espanol": "Evidencia"},
            {"ingles": "To assume", "pronunciacion": "tu a-sium", "espanol": "Asumir / Suponer"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'evidence'?", "respuesta_correcta": "evidencia",
             "alternativas": ["evidencia", "prueba"], "pista": "Lo que demuestra algo."},
            {"pregunta": "Como dices 'investigar' (sustantivo) en ingles?", "respuesta_correcta": "research",
             "alternativas": ["research", "researching"], "pista": "Buscar conocimiento."},
        ],
    },
    {
        "id": "B2-09", "nivel": "B2", "nombre": "Expresiones para debates",
        "objetivo": "Participar en discusiones argumentadas",
        "vocabulario": [
            {"ingles": "From my point of view...", "pronunciacion": "from mai point of viu", "espanol": "Desde mi punto de vista..."},
            {"ingles": "I strongly believe that...", "pronunciacion": "ai strong-li bi-liv zat", "espanol": "Creo firmemente que..."},
            {"ingles": "There is no doubt that...", "pronunciacion": "zer is no daut zat", "espanol": "No hay duda de que..."},
            {"ingles": "On the one hand... on the other hand...", "pronunciacion": "on de uan jand", "espanol": "Por un lado... por el otro..."},
        ],
        "preguntas": [
            {"pregunta": "Como introduces tu punto de vista?", "respuesta_correcta": "from my point of view",
             "alternativas": ["from my point of view"], "pista": "View = vista."},
            {"pregunta": "Que significa 'there is no doubt'?", "respuesta_correcta": "no hay duda",
             "alternativas": ["no hay duda"], "pista": "Expresa certeza."},
        ],
    },
    {
        "id": "B2-10", "nivel": "B2", "nombre": "Vocabulario de salud y bienestar",
        "objetivo": "Hablar sobre salud fisica y mental",
        "vocabulario": [
            {"ingles": "Mental health", "pronunciacion": "men-tal jelt", "espanol": "Salud mental"},
            {"ingles": "Workout", "pronunciacion": "uork-aut", "espanol": "Entrenamiento"},
            {"ingles": "To stay fit", "pronunciacion": "tu stei fit", "espanol": "Mantenerse en forma"},
            {"ingles": "Balanced diet", "pronunciacion": "ba-lanst da-yet", "espanol": "Dieta balanceada"},
            {"ingles": "Wellness", "pronunciacion": "uel-nes", "espanol": "Bienestar"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'mantenerse en forma'?", "respuesta_correcta": "to stay fit",
             "alternativas": ["to stay fit", "stay fit"], "pista": "Fit = en forma."},
            {"pregunta": "Que significa 'workout'?", "respuesta_correcta": "entrenamiento",
             "alternativas": ["entrenamiento", "ejercicio"], "pista": "Rutina de ejercicios."},
        ],
    },
]

# ============================================================
# NIVEL C1 - Avanzado (Dominio operativo eficaz)
# ============================================================
TEMARIO_C1 = [
    {
        "id": "C1-01", "nivel": "C1", "nombre": "Expresiones avanzadas de argumentacion",
        "objetivo": "Construir argumentos sofisticados",
        "vocabulario": [
            {"ingles": "Be that as it may", "pronunciacion": "bi zat as it mei", "espanol": "Sea como fuere"},
            {"ingles": "That said", "pronunciacion": "zat sed", "espanol": "Dicho esto"},
            {"ingles": "By and large", "pronunciacion": "bai and lary", "espanol": "En general"},
            {"ingles": "In light of", "pronunciacion": "in lait of", "espanol": "A la luz de"},
            {"ingles": "Notwithstanding", "pronunciacion": "not-uiz-stan-ding", "espanol": "A pesar de"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'in light of'?", "respuesta_correcta": "a la luz de",
             "alternativas": ["a la luz de", "considerando"], "pista": "Considerando nueva informacion."},
            {"pregunta": "Como introduces una conclusion formal?", "respuesta_correcta": "that said",
             "alternativas": ["that said", "having said that"], "pista": "Dicho esto."},
        ],
    },
    {
        "id": "C1-02", "nivel": "C1", "nombre": "Phrasal verbs avanzados",
        "objetivo": "Dominar phrasal verbs complejos",
        "vocabulario": [
            {"ingles": "Pull through", "pronunciacion": "pul zru", "espanol": "Sobrevivir / Salir adelante"},
            {"ingles": "Come up with", "pronunciacion": "com ap uiz", "espanol": "Idear / Inventar"},
            {"ingles": "Get away with", "pronunciacion": "get a-uei uiz", "espanol": "Salirse con la suya"},
            {"ingles": "Set up", "pronunciacion": "set ap", "espanol": "Establecer"},
            {"ingles": "Bring about", "pronunciacion": "bring a-baut", "espanol": "Causar"},
            {"ingles": "Call off", "pronunciacion": "kol of", "espanol": "Cancelar"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'come up with'?", "respuesta_correcta": "idear",
             "alternativas": ["idear", "inventar", "pensar"], "pista": "Crear una idea o solucion."},
            {"pregunta": "Como dices 'cancelar' como phrasal verb?", "respuesta_correcta": "call off",
             "alternativas": ["call off", "cancel"], "pista": "Off = fuera."},
        ],
    },
    {
        "id": "C1-03", "nivel": "C1", "nombre": "Vocabulario academico avanzado",
        "objetivo": "Escribir ensayos y articulos academicos",
        "vocabulario": [
            {"ingles": "To ascertain", "pronunciacion": "tu a-ser-ttein", "espanol": "Averiguar / Determinar"},
            {"ingles": "To undermine", "pronunciacion": "tu an-der-main", "espanol": "Socavar"},
            {"ingles": "Comprehensive", "pronunciacion": "com-pre-jen-siv", "espanol": "Exhaustivo"},
            {"ingles": "To encompass", "pronunciacion": "tu en-com-pas", "espanol": "Abarcar"},
            {"ingles": "Conducive", "pronunciacion": "con-diu-siv", "espanol": "Favorable / Propicio"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'comprehensive'?", "respuesta_correcta": "exhaustivo",
             "alternativas": ["exhaustivo", "completo"], "pista": "Que cubre todo."},
            {"pregunta": "Como dices 'socavar' en ingles?", "respuesta_correcta": "to undermine",
             "alternativas": ["to undermine", "undermine"], "pista": "Debilitar por debajo."},
        ],
    },
    {
        "id": "C1-04", "nivel": "C1", "nombre": "Subjuntivo y oraciones avanzadas",
        "objetivo": "Usar estructuras gramaticales complejas",
        "vocabulario": [
            {"ingles": "I suggest that he go", "pronunciacion": "ai su-yest zat ji gou", "espanol": "Sugiero que el vaya"},
            {"ingles": "It's essential that she be there", "pronunciacion": "its esen-shal zat shi bi der", "espanol": "Es esencial que ella este alli"},
            {"ingles": "If only I had known", "pronunciacion": "if on-li ai jav noun", "espanol": "Si tan solo hubiera sabido"},
            {"ingles": "Had I known, I would have...", "pronunciacion": "jad ai noun ai wuod jav", "espanol": "De haber sabido, habria..."},
        ],
        "preguntas": [
            {"pregunta": "Completa: I suggest that he ___ (ir)", "respuesta_correcta": "go",
             "alternativas": ["go", "should go"], "pista": "Subjuntivo: verbo en base."},
            {"pregunta": "Que significa 'if only'?", "respuesta_correcta": "si tan solo",
             "alternativas": ["si tan solo", "ojala"], "pista": "Expresa deseo sobre el pasado."},
        ],
    },
    {
        "id": "C1-05", "nivel": "C1", "nombre": "Vocabulario de medios y noticias",
        "objetivo": "Comprender y discutir noticias",
        "vocabulario": [
            {"ingles": "Breaking news", "pronunciacion": "brei-king nius", "espanol": "Noticia de ultima hora"},
            {"ingles": "Headline", "pronunciacion": "jed-lain", "espanol": "Titular"},
            {"ingles": "Press conference", "pronunciacion": "pres con-fe-rens", "espanol": "Conferencia de prensa"},
            {"ingles": "To broadcast", "pronunciacion": "tu broad-cast", "espanol": "Transmitir / Difundir"},
            {"ingles": "Censorship", "pronunciacion": "sen-sor-ship", "espanol": "Censura"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'titular' de noticia?", "respuesta_correcta": "headline",
             "alternativas": ["headline"], "pista": "Titulo de una noticia."},
            {"pregunta": "Que significa 'broadcast'?", "respuesta_correcta": "transmitir",
             "alternativas": ["transmitir", "difundir"], "pista": "Emitir por radio o TV."},
        ],
    },
    {
        "id": "C1-06", "nivel": "C1", "nombre": "Inversion y enfasis",
        "objetivo": "Usar estructuras enfaticas formales",
        "vocabulario": [
            {"ingles": "Not only did he..., but he also...", "pronunciacion": "not on-li did ji", "espanol": "No solo... sino tambien..."},
            {"ingles": "Under no circumstances should you...", "pronunciacion": "an-der no cir-cum-stan-shes shud iu", "espanol": "Bajo ninguna circunstancia debes..."},
            {"ingles": "Rarely have I seen...", "pronunciacion": "rer-li jav ai sin", "espanol": "Rara vez he visto..."},
        ],
        "preguntas": [
            {"pregunta": "Completa: Not only ___ he win, but he also broke the record", "respuesta_correcta": "did",
             "alternativas": ["did"], "pista": "Inversion: did + sujeto + verbo."},
        ],
    },
    {
        "id": "C1-07", "nivel": "C1", "nombre": "Vocabulario de finanzas",
        "objetivo": "Hablar sobre economia y finanzas",
        "vocabulario": [
            {"ingles": "Assets", "pronunciacion": "a-sets", "espanol": "Activos"},
            {"ingles": "Liabilities", "pronunciacion": "lai-a-bi-li-tis", "espanol": "Pasivos"},
            {"ingles": "Inflation", "pronunciacion": "in-flei-shon", "espanol": "Inflacion"},
            {"ingles": "To invest", "pronunciacion": "tu in-vest", "espanol": "Invertir"},
            {"ingles": "Profit margin", "pronunciacion": "pro-fit mar-yin", "espanol": "Margen de ganancia"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'inflation'?", "respuesta_correcta": "inflacion",
             "alternativas": ["inflacion"], "pista": "Subida generalizada de precios."},
            {"pregunta": "Como dices 'invertir' (dinero)?", "respuesta_correcta": "to invest",
             "alternativas": ["to invest", "invest"], "pista": "Poner dinero esperando ganancias."},
        ],
    },
    {
        "id": "C1-08", "nivel": "C1", "nombre": "Discurso persuasivo",
        "objetivo": "Persuadir y convencer",
        "vocabulario": [
            {"ingles": "To advocate for", "pronunciacion": "tu ad-vo-keit for", "espanol": "Abogar por"},
            {"ingles": "Compelling", "pronunciacion": "com-pe-ling", "espanol": "Convincente"},
            {"ingles": "To address concerns", "pronunciacion": "tu a-dres con-cerns", "espanol": "Abordar preocupaciones"},
            {"ingles": "Plausible", "pronunciacion": "plo-si-bol", "espanol": "Razonable / Plausible"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'compelling'?", "respuesta_correcta": "convincente",
             "alternativas": ["convincente", "atractivo"], "pista": "Que persuade."},
            {"pregunta": "Como dices 'abogar por'?", "respuesta_correcta": "to advocate for",
             "alternativas": ["to advocate for", "advocate for"], "pista": "Defender una causa."},
        ],
    },
    {
        "id": "C1-09", "nivel": "C1", "nombre": "Vocabulario legal basico",
        "objetivo": "Comprender terminologia legal comun",
        "vocabulario": [
            {"ingles": "To sue", "pronunciacion": "tu su", "espanol": "Demandar (legalmente)"},
            {"ingles": "Court hearing", "pronunciacion": "cort jier-ing", "espanol": "Audiencia judicial"},
            {"ingles": "Defendant", "pronunciacion": "de-fen-dant", "espanol": "Acusado / Demandado"},
            {"ingles": "Plaintiff", "pronunciacion": "plein-tif", "espanol": "Demandante"},
            {"ingles": "Settlement", "pronunciacion": "set-el-ment", "espanol": "Acuerdo / Liquidacion"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'demandar' (legalmente)?", "respuesta_correcta": "to sue",
             "alternativas": ["to sue", "sue"], "pista": "Llevar a juicio."},
            {"pregunta": "Que significa 'plaintiff'?", "respuesta_correcta": "demandante",
             "alternativas": ["demandante"], "pista": "Quien inicia la demanda."},
        ],
    },
    {
        "id": "C1-10", "nivel": "C1", "nombre": "Expresiones idiomaticas avanzadas",
        "objetivo": "Usar modismos sofisticados",
        "vocabulario": [
            {"ingles": "A blessing in disguise", "pronunciacion": "a blesing in dis-gua-is", "espanol": "Una bendicion disfrazada"},
            {"ingles": "Bite off more than you can chew", "pronunciacion": "bait of mor zan iu kan chu", "espanol": "Abocar mas de lo que puedes masticar"},
            {"ingles": "To cut corners", "pronunciacion": "tu kat cor-nerz", "espanol": "Tomar atajos"},
            {"ingles": "Once in a blue moon", "pronunciacion": "uans in a blu mun", "espanol": "Muy rara vez"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'once in a blue moon'?", "respuesta_correcta": "muy rara vez",
             "alternativas": ["muy rara vez", "casi nunca"], "pista": "Algo que pasa muy poco."},
            {"pregunta": "Que significa 'blessing in disguise'?", "respuesta_correcta": "bendicion disfrazada",
             "alternativas": ["bendicion disfrazada"], "pista": "Algo malo que resulta bueno."},
        ],
    },
]

# ============================================================
# NIVEL C2 - Maestria (Dominio)
# ============================================================
TEMARIO_C2 = [
    {
        "id": "C2-01", "nivel": "C2", "nombre": "Registro literario",
        "objetivo": "Comprender y usar lenguaje literario",
        "vocabulario": [
            {"ingles": "Ephemeral", "pronunciacion": "e-fe-me-ral", "espanol": "Efimero (que dura poco)"},
            {"ingles": "Semblance", "pronunciacion": "sem-blans", "espanol": "Apariencia"},
            {"ingles": "Quintessential", "pronunciacion": "quin-ti-sen-shal", "espanol": "Quintaesencial"},
            {"ingles": "Pernicious", "pronunciacion": "per-ni-shos", "espanol": "Pernicioso"},
            {"ingles": "Ubiquitous", "pronunciacion": "iu-bic-ui-tos", "espanol": "Ubicuo"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'ephemeral'?", "respuesta_correcta": "efimero",
             "alternativas": ["efimero", "pasaiero"], "pista": "Que dura poco tiempo."},
            {"pregunta": "Que significa 'ubiquitous'?", "respuesta_correcta": "ubicuo",
             "alternativas": ["ubicuo", "omnipresente"], "pista": "Que esta en todos lados."},
        ],
    },
    {
        "id": "C2-02", "nivel": "C2", "nombre": "Estructuras complejas",
        "objetivo": "Hablar con fluidez nativa",
        "vocabulario": [
            {"ingles": "Notwithstanding the fact that", "pronunciacion": "not-uiz-stan-ding de fact zat", "espanol": "No obstante el hecho de que"},
            {"ingles": "Be that as it may", "pronunciacion": "bi zat as it mei", "espanol": "Sea como fuere"},
            {"ingles": "Needless to say", "pronunciacion": "ni-dles tu sei", "espanol": "Ni hace falta decir"},
            {"ingles": "In the grand scheme of things", "pronunciacion": "in de grand skim of zings", "espanol": "En el gran esquema de las cosas"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'needless to say'?", "respuesta_correcta": "ni hace falta decir",
             "alternativas": ["ni hace falta decir", "obviamente"], "pista": "Algo evidente."},
            {"pregunta": "Que significa 'be that as it may'?", "respuesta_correcta": "sea como fuere",
             "alternativas": ["sea como fuere", "de todos modos"], "pista": "Expresion para conceder un punto."},
        ],
    },
    {
        "id": "C2-03", "nivel": "C2", "nombre": "Vocabulario filosofico y abstracto",
        "objetivo": "Discutir conceptos abstractos",
        "vocabulario": [
            {"ingles": "Existential", "pronunciacion": "ex-is-ten-shal", "espanol": "Existencial"},
            {"ingles": "Conundrum", "pronunciacion": "co-non-drom", "espanol": "Dilema / Problema"},
            {"ingles": "Nuanced", "pronunciacion": "niu-anst", "espanol": "Matizado"},
            {"ingles": "Pragmatic", "pronunciacion": "prag-ma-tic", "espanol": "Pragmatico"},
            {"ingles": "Paradigm shift", "pronunciacion": "pa-ra-daim shift", "espanol": "Cambio de paradigma"},
        ],
        "preguntas": [
            {"pregunta": "Que significa 'nuanced'?", "respuesta_correcta": "matizado",
             "alternativas": ["matizado", "con sutilezas"], "pista": "Con muchos detalles sutiles."},
            {"pregunta": "Como dices 'cambio de paradigma'?", "respuesta_correcta": "paradigm shift",
             "alternativas": ["paradigm shift"], "pista": "Un cambio fundamental en la forma de pensar."},
        ],
    },
    {
        "id": "C2-04", "nivel": "C2", "nombre": "Vocabulario cientifico avanzado",
        "objetivo": "Comprender textos cientificos",
        "vocabulario": [
            {"ingles": "Hypothesis", "pronunciacion": "jai-po-ze-sis", "espanol": "Hipotesis"},
            {"ingles": "To validate", "pronunciacion": "tu va-li-deit", "espanol": "Validar"},
            {"ingles": "Empirical", "pronunciacion": "em-pi-ri-cal", "espanol": "Empirico"},
            {"ingles": "Peer review", "pronunciacion": "pir ri-viu", "espanol": "Revision por pares"},
            {"ingles": "Data set", "pronunciacion": "dei-ta set", "espanol": "Conjunto de datos"},
        ],
        "preguntas": [
            {"pregunta": "Como dices 'conjunto de datos'?", "respuesta_correcta": "data set",
             "alternativas": ["data set", "dataset"], "pista": "Coleccion de datos."},
        ],
    },
    {
        "id": "C2-05", "nivel": "C2", "nombre": "Refranes y dichos populares",
        "objetivo": "Conocer proverbios en ingles",
        "vocabulario": [
            {"ingles": "Actions speak louder than words", "pronunciacion": "ac-shons spik lau-der zan uerds", "espanol": "Las acciones valen mas que las palabras"},
            {"ingles": "The early bird catches the worm", "pronunciacion": "de er-li berd ca-ches de uorm", "espanol": "El que madruga, Dios le ayuda"},
            {"ingles": "Better late than never", "pronunciacion": "be-ter leit zan ne-ver", "espanol": "Mas vale tarde que nunca"},
            {"ingles": "Practice makes perfect", "pronunciacion": "prac-tis meiks per-fect", "espanol": "La practica hace al maestro"},
        ],
        "preguntas": [
            {"pregunta": "Que proverbio significa 'la practica hace al maestro'?", "respuesta_correcta": "practice makes perfect",
             "alternativas": ["practice makes perfect"], "pista": "Practice = practica."},
            {"pregunta": "Que significa 'better late than never'?", "respuesta_correcta": "mas vale tarde que nunca",
             "alternativas": ["mas vale tarde que nunca"], "pista": "Es mejor tarde que no hacerlo."},
        ],
    },
]

# ============================================================
# Diccionario completo por niveles
# ============================================================
TODOS_NIVELES = {
    "A1": {"nombre": "A1 - Principiante", "descripcion": "Saludos, vocabulario basico, presente simple",
           "lecciones": TEMARIO_A1, "color": "#10b981", "emoji": "🌱"},
    "A2": {"nombre": "A2 - Elemental", "descripcion": "Rutinas, pasado simple, modales basicos",
           "lecciones": TEMARIO_A2, "color": "#3b82f6", "emoji": "🌿"},
    "B1": {"nombre": "B1 - Intermedio", "descripcion": "Presente perfecto, opiniones, condicionales",
           "lecciones": TEMARIO_B1, "color": "#8b5cf6", "emoji": "🌳"},
    "B2": {"nombre": "B2 - Intermedio alto", "descripcion": "Negocios, expresiones, voz pasiva",
           "lecciones": TEMARIO_B2, "color": "#f59e0b", "emoji": "🎯"},
    "C1": {"nombre": "C1 - Avanzado", "descripcion": "Argumentacion, vocabulario avanzado",
           "lecciones": TEMARIO_C1, "color": "#ef4444", "emoji": "🚀"},
    "C2": {"nombre": "C2 - Maestria", "descripcion": "Literario, filosofico, matices sutiles",
           "lecciones": TEMARIO_C2, "color": "#7c3aed", "emoji": "👑"},
}

ORDEN_NIVELES = ["A1", "A2", "B1", "B2", "C1", "C2"]


def obtener_niveles():
    """Retorna la lista ordenada de niveles disponibles"""
    return ORDEN_NIVELES


def obtener_info_nivel(nivel):
    """Retorna la informacion de un nivel especifico"""
    return TODOS_NIVELES.get(nivel.upper())


def obtener_lecciones_nivel(nivel):
    """Retorna todas las lecciones de un nivel"""
    info = obtener_info_nivel(nivel)
    return info["lecciones"] if info else []


def obtener_leccion(nivel, leccion_id):
    """Busca una leccion por su ID"""
    lecciones = obtener_lecciones_nivel(nivel)
    for l in lecciones:
        if l["id"] == leccion_id:
            return l
    return None


def total_lecciones_nivel(nivel):
    """Cuenta las lecciones de un nivel"""
    return len(obtener_lecciones_nivel(nivel))


def total_lecciones_todos():
    """Cuenta todas las lecciones de todos los niveles"""
    return sum(total_lecciones_nivel(n) for n in obtener_niveles())


def siguiente_nivel(nivel_actual):
    """Retorna el siguiente nivel, o None si es el ultimo"""
    if nivel_actual.upper() in ORDEN_NIVELES:
        idx = ORDEN_NIVELES.index(nivel_actual.upper())
        if idx < len(ORDEN_NIVELES) - 1:
            return ORDEN_NIVELES[idx + 1]
    return None


def nivel_anterior(nivel_actual):
    """Retorna el nivel anterior, o None si es el primero"""
    if nivel_actual.upper() in ORDEN_NIVELES:
        idx = ORDEN_NIVELES.index(nivel_actual.upper())
        if idx > 0:
            return ORDEN_NIVELES[idx - 1]
    return None


def validar_respuesta(respuesta_usuario, pregunta):
    """Valida si la respuesta del usuario es correcta (acepta alternativas)"""
    if not respuesta_usuario:
        return False
    respuesta_limpia = re.sub(r"[^\w\s]", "", respuesta_usuario.strip().lower())
    for alt in pregunta.get("alternativas", []):
        alternativa_limpia = re.sub(r"[^\w\s]", "", alt.strip().lower())
        if alternativa_limpia in respuesta_limpia or respuesta_limpia in alternativa_limpia:
            return True
    return False


def siguiente_pregunta_aleatoria(leccion, indices_excluidos=None):
    """Retorna el indice y la siguiente pregunta aleatoria no respondida"""
    preguntas = leccion["preguntas"]
    disponibles = [i for i in range(len(preguntas))
                    if indices_excluidos is None or i not in indices_excluidos]
    if not disponibles:
        return None, None
    indice = random.choice(disponibles)
    return indice, preguntas[indice]


def obtener_primera_leccion(nivel):
    """Retorna la primera leccion del nivel o None"""
    lecciones = obtener_lecciones_nivel(nivel)
    return lecciones[0] if lecciones else None


def obtener_siguiente_leccion(nivel, leccion_actual_id):
    """Retorna la siguiente leccion del nivel, o None si era la ultima"""
    lecciones = obtener_lecciones_nivel(nivel)
    for i, l in enumerate(lecciones):
        if l["id"] == leccion_actual_id:
            if i + 1 < len(lecciones):
                return lecciones[i + 1]
    return None

