from guizero import App, PushButton, Text, Picture, Box, TextBox
from pygame import mixer
import subprocess
import random
import time
import sys 

# Este contador, reinicia (n.veces pasas por la mazmorra, en el caso de reiniciar el juego)

reiniciar_contador = False

#Definición acciones del juego:

def historia_princesa(inicio):
    global reiniciar_contador
    reiniciar_contador = True
    global app_historia_princesa
    app_historia = App(title="HISTORIA PRINCESA", width=800, height=600)
    app_historia.bg = obtener_color_pastel()
    text = Text(app_historia, text="\nQuerida princesa, vas caminando por un sendero 👣 mientras disfrutas de tu paseo por el bonito bosque 🌲🌲🌲", size=14)
    text = Text(app_historia, text="\nMientras caminas 👣, ves un bonito castillo 🏰. Te preguntas qué habrá allí?\n\n¡Vamos, que voy...\n", size=14)
    image = Picture(app_historia, image="imagenes/castillo.png", width=640, height=480)
    text = Text(app_historia, text="\n")
    boton_continuar = PushButton(app_historia, text="Continuar", command=camino, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_historia.full_screen = True
    app_historia.display()

def camino():
    global app_camino
    app_camino = App(title="PASEO POR EL CAMINO", width=800, height=600)
    app_camino.bg = obtener_color_pastel()
    text = Text(app_camino, text="\nEn tu paseo, a lo lejos, ves 👀 venir unos guardias🗡️🐎.\n\n¿Qué haces?\n", size=14)
    image = Picture(app_camino, image="imagenes/guardia.png", width=640, height=480)
    text = Text(app_camino, text="\n")
    boton_escondes = PushButton(app_camino, text="Te escondes", command=escondes, width=20)
    boton_escondes.bg = "#FFFFFF"
    boton_escondes.font = "bold"
    boton_continuar = PushButton(app_camino, text="Continuar", command=continuas, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_camino.full_screen = True
    app_camino.display()

def escondes():
    global app_escondes
    app_escondes = App(title="Te escondes", width=800, height=600)
    app_escondes.bg = obtener_color_pastel()
    text = Text(app_escondes, text="\nTe escondes...👏 eso ha sido una sabia decisión.\n\nNo sabemos si los guardias eran amigos o no.\n\nPara poder salir del escondite, debes resolver una operación matemática📱.", size=14)
    
    num1 = random.randint(1, 20)
    num2 = random.randint(1, num1)
    operator = random.choice(['+', '-'])
    formula = f"{num1} {operator} {num2} = ?"
    
    text_formula = Text(app_escondes, text="" + formula, size=14)
    input_box = TextBox(app_escondes)
    image = Picture(app_escondes, image="imagenes/bosque.png", width=640, height=480)
       
    def verificar_respuesta():
        respuesta = int(input_box.value)
        if operator == '+':
            resultado = num1 + num2
        elif operator == '-':
            resultado = num1 - num2
        if respuesta == resultado:
            text_formula.value = "\n\n¡Correcto!\n\n"
            boton_continuar = PushButton(app_escondes, text="Continuar", command=continuas, width=20)
            boton_continuar.bg = "#FFFFFF"
            boton_continuar.font = "bold"
        else:
            text_formula.value = "Respuesta incorrecta"

    boton_resolver = PushButton(app_escondes, text="Resolver", command=verificar_respuesta, width=20)
    boton_resolver.bg = "#FFFFFF"
    boton_resolver.font = "bold"
    
    app_escondes.full_screen = True
    app_escondes.display()

def continuas():
    global app_continuas
    app_continuas = App(title="CONTINUAS", width=800, height=600)
    app_continuas.bg = obtener_color_pastel()
    text = Text(app_continuas, text="\nContinúas caminand👣... y\n", size=14)
    image = Picture(app_continuas, image="imagenes/camino.png", width=640, height=480)
    text = Text(app_continuas, text="\n")
    boton_continuar = PushButton(app_continuas, text="Continuar", command=te_atrapan, width=20)
    app_continuas.full_screen = True
    app_continuas.display()

def te_atrapan():
    if random.choice([True, False]):
        mazmorra()
    else:
        castillo()

def castillo():
    global app_castillo
    app_castillo = App(title="CASTILLO", width=800, height=600)
    app_castillo.bg = obtener_color_pastel()
    text = Text(app_castillo, text="\nLlegas al castillo 🏰... Parece estar encantado👻.. ¿Qué haces?\n", size=14)
    image = Picture(app_castillo, image="imagenes/puertacastillo.png", width=640, height=480)
    text = Text(app_castillo, text="\n")

    def decision_entras():
        app_castillo.hide()
        entras()

    def decision_te_das_la_vuelta():
        app_castillo.hide()
        vuelta()

    boton_entras = PushButton(app_castillo, text="Entras", command=decision_entras, width=20)
    boton_entras.bg = "#FFFFFF"
    boton_entras.font = "bold"
    boton_te_das_la_vuelta = PushButton(app_castillo, text="Te das la vuelta", command=decision_te_das_la_vuelta, width=20)
    boton_te_das_la_vuelta.bg = "#FFFFFF"
    boton_te_das_la_vuelta.font = "bold"
    app_castillo.full_screen = True
    app_castillo.display()

def vuelta():
    app_vuelta = App(title="REGRESO")
    app_vuelta.full_screen = True
    app_vuelta.bg = obtener_color_pastel()

    # Generar una elección aleatoria entre 1 y 2
    eleccion = random.randint(1, 2)

    if eleccion == 1:
        # Ir a la función mazmorra()
        mazmorra()
    else:
        # Ir a la función hablar_campesino()
        hablar_campesino()

    app_vuelta.display()

def entras():
    app_entras = App(title="REGRESO")
    app_entras.full_screen = True
    app_entras.bg = obtener_color_pastel()
    
    try:
        # Llamar al programa cesar.py usando subprocess.Popen
        proceso_cesar = subprocess.Popen(["python", "cesar.py"])
        proceso_cesar.wait()  # Esperar a que el proceso del juego termine
    except Exception as e:
        # Manejar cualquier error al ejecutar cesar.py
        print("Error al ejecutar cesar.py:", e)

    # Llamar a la función entrada_castillo()

    app_castillo.hide()
    app_entras.destroy()
    entrada_castillo()

def entrada_castillo():
    global app_entrada_castillo
    app_entrada_castillo = App(title="ENTRADA CASTILLO", width=800, height=600)
    app_entrada_castillo.bg = obtener_color_pastel()
    text = Text(app_entrada_castillo, text="\n¡Princesa... FELICIDADES! Has entrado al castillo encantado🏰. Te encuentras con 3 puertas 🚪🚪🚪. ¿Cuál vas a abrir?\n", size=14)
    image = Picture(app_entrada_castillo, image="imagenes/entrada.png", width=640, height=480)
    text = Text(app_entrada_castillo, text="\n")

    def abrir_puerta(numero_puerta):
        app_entrada_castillo.hide()
        mensaje = f"Has abierto la puerta {numero_puerta}."
        Text(app_entrada_castillo, text=mensaje)
        app_entrada_castillo.show()

    boton_opcion_derecha = PushButton(app_entrada_castillo, text="Derecha📜", command=biblioteca, width=20)
    boton_opcion_derecha.bg = "#FFFFFF"
    boton_opcion_derecha.font = "bold"
    boton_opcion_medio = PushButton(app_entrada_castillo, text="Medio 🚪", command=salir_mazmorra, width=20)
    boton_opcion_medio.bg = "#FFFFFF"
    boton_opcion_medio.font = "bold"
    boton_opcion_izquierda = PushButton(app_entrada_castillo, text="Izquierda 🌻", command=jardin, width=20)
    boton_opcion_izquierda.bg = "#FFFFFF"
    boton_opcion_izquierda.font = "bold"
    app_entrada_castillo.full_screen = True
    app_entrada_castillo.display()

def biblioteca():
    global app_biblioteca
    app_biblioteca = App(title="BIBLIOTECA", width=800, height=600)
    app_biblioteca.bg = obtener_color_pastel()
    text = Text(app_biblioteca, text="\nWowww la 🏰 biblioteca del castillo, está llena de libros y papiros interesantes 📜.", size=14)
    text = Text(app_biblioteca, text="\nTe gusta mucho leer? Pero tambien quieres ver más 🤔 Qué haces?❓\n", size=14)
    image = Picture(app_biblioteca, image="imagenes/biblioteca.png", width=640, height=480)
    text = Text(app_biblioteca, text="\n")
    def decision_leer():
        app_biblioteca.hide()
        mazmorra()

    def decision_continuar():
        app_biblioteca.hide()
        cocina()
    boton_leer = PushButton(app_biblioteca, text="Te paras a leer", command=decision_leer, width=20)
    boton_leer.bg = "#FFFFFF"
    boton_leer.font = "bold"
    boton_continuar = PushButton(app_biblioteca, text="Continúas", command=salir_mazmorra, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_biblioteca.full_screen = True
    app_biblioteca.display()

# Contador de mazmorra

contador_mazmorra = 0 
contador_mazmorra_maximo = 3 #máximo de pasos por la mazmorra para Game over (3)
reiniciar_contador = False

def mazmorra():
    global app_mazmorra, contador_mazmorra, reiniciar_contador
    
    if reiniciar_contador:
        contador_mazmorra = 0
        reiniciar_contador = False
    
    contador_mazmorra += 1 # Te avisa!!
    app_mazmorra = App(title="MAZMORRA OSCURA", width=800, height=600)
    app_mazmorra.bg = obtener_color_pastel()
    text = Text(app_mazmorra, text="\nOOOHHHHH!!!! Te han capturado⛓️!! Ahora te encuentras encerrada 🔒", size=14)
    text = Text(app_mazmorra, text="\nEn las mazmorras, triste 😔, ojerosa, entre lágrimas 😢... ves que hay un esqueleto 💀.", size=14)
    text = Text(app_mazmorra, text="\nEl esqueleto tiene una 🔑, pero aparece un 🐭 y te ofrece su ayuda.", size=14)
    text = Text(app_mazmorra, text="\n¿Qué haces?\n", size=14)
    image = Picture(app_mazmorra, image="imagenes/mazmorra.png", width=640, height=480)
    
    if contador_mazmorra == 2:
        pantalla_adicional()
    elif contador_mazmorra >= contador_mazmorra_maximo: 
        pantalla_adicional_nueva()
    else:
        boton_coges_llave = PushButton(app_mazmorra, text="Coges la llave", command=respuesta_intoxicacion, width=20)
        boton_coges_llave.bg = "#FFFFFF"
        boton_coges_llave.font = "bold"
    
    boton_ayuda_raton = PushButton(app_mazmorra, text="Te ayuda el ratón", command=respuesta_ayuda, width=20)
    boton_ayuda_raton.bg = "#FFFFFF"
    boton_ayuda_raton.font = "bold"
    
    app_mazmorra.full_screen = True
    app_mazmorra.display()
    
#cuando pasas dos veces por la mazmorra te avisa con esta pantalla

def pantalla_adicional():
    app_adicional = App(title="Pantalla Adicional", width=800, height=600)
    app_adicional.bg = obtener_color_pastel()
    text = Text(app_adicional, text="\n\n ¿Recuerdas qué es la mazmorra 🛑?\n\nYa has estado aquí, ¡vigila y no vuelvas🔙! \n\nNo siempre podré ayudarte.\n", size=14)
    image = Picture(app_adicional, image="imagenes/raton2.png", width=640, height=480)
    text = Text(app_adicional, text="\n")
    boton_continuar = PushButton(app_adicional, text="Continuar", command=salir_mazmorra, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_adicional.full_screen = True
    app_adicional.display()

#cuando pasas 3 veces por la mazmorra te mata game over, te da dos opciones.

def pantalla_adicional_nueva():
    app_adicional_nueva = App(title="Pantalla Adicional Game Over", width=800, height=600)
    app_adicional_nueva.bg = obtener_color_pastel()
    text = Text(app_adicional_nueva, text="\n\nTe lo dije⚠️.. ya has pasado por la mazmorra demasiadas veces⏳. Tal y como estoy... no te puedo ayudar... ⚰️🪦!!!\n\nLo siento... has llegado hasta aquí🔚.\n\nDecide qué hacer a continuación.", size=14)
    image = Picture(app_adicional_nueva, image="imagenes/raton3.png", width=640, height=480)
    text = Text(app_adicional_nueva, text="\n")
    boton_continuar = PushButton(app_adicional_nueva, text="Continuar", command=game_over, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_adicional_nueva.full_screen = True
    app_adicional_nueva.display()

def respuesta_ayuda():
    global app_respuesta
    app_respuesta = App(title="EL RATÓN TE AYUDA", width=800, height=600)
    app_respuesta.bg = obtener_color_pastel()
    text = Text(app_respuesta, text="\nTienes un nuevo amigo, el 🐭 coge la 🔑 por ti, juntos salís de la mazmorra", size=14)
    text = Text(app_respuesta, text="\nCamináis por un largo pasillo ....\n", size=14)
    image = Picture(app_respuesta, image="imagenes/raton.png", width=640, height=480)
    text = Text(app_respuesta, text="\n")
    boton_continuar = PushButton(app_respuesta, text="Continuar", command=salir_mazmorra, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_respuesta.full_screen = True
    app_respuesta.display()

def respuesta_intoxicacion():
    global app_respuesta
    app_respuesta = App(title="INTOXICACIÓN", width=800, height=600)
    app_respuesta.bg = obtener_color_pastel()

    def verificar_respuesta():
        respuesta = int(input_box.value)
        if respuesta == resultado:
            app_respuesta.hide()
            salir_mazmorra()
        else:
            text.value = "\n\nRespuesta incorrecta. Vuelve a intentarlo."
            input_box.clear()

# Fórmula aleatoria con * multiplicación

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    resultado = num1 * num2
    text = Text(app_respuesta, text="\nOHHH!!!!!!\n\nEl esqueleto 💀 tiene una bacteria 🦠 y te has intoxicado 🤢...", size=14)
    text = Text(app_respuesta, text=f"\nPara recuperarte 🩹, resuelve la siguienteoperación matemática 💭: {num1} * {num2}", size=14)
    text = Text(app_respuesta, text="\n")
    image = Picture(app_respuesta, image="imagenes/raton.png", width=640, height=480)
    text = Text(app_respuesta, text="\n")
    input_box = TextBox(app_respuesta)
    text = Text(app_respuesta, text="\n")
    boton = PushButton(app_respuesta, text="Continuar", command=verificar_respuesta, width=20)
    boton.bg = "#FFFFFF"
    boton.font = "bold"
    app_respuesta.full_screen = True
    app_respuesta.display()

def salir_mazmorra():
    global app_salir_mazmorra
    app_salir_mazmorra = App(title="MAZMORRA OSCURA", width=800, height=600)
    app_salir_mazmorra.bg = obtener_color_pastel()
    text = Text(app_salir_mazmorra, text="\n Has llegado a un pasillo hay tres puertas 🚪🚪🚪, Cuál vas ha abrir?...\n", size=14)
    image = Picture(app_salir_mazmorra, image="imagenes/puertas.png", width=640, height=480)
    text = Text(app_salir_mazmorra, text="\n")
    
    def abrir_puerta(numero_puerta):
        app_salir_mazmorra.hide()
        mensaje = f"Has abierto la puerta {numero_puerta}.",
        Text(app_salir_mazmorra, text=mensaje)
        app_salir_mazmorra.show()
    
    boton_opcion = PushButton(app_salir_mazmorra, text="Derecha🍽️", command=cocina, width=20)
    boton_opcion.bg = "#FFFFFF"
    boton_opcion.font = "bold"
    boton_opcion = PushButton(app_salir_mazmorra, text="medio 🛏️", command=habitacion, width=20)
    boton_opcion.bg = "#FFFFFF"
    boton_opcion.font = "bold"
    boton_opcion = PushButton(app_salir_mazmorra, text="Izquierda👑 ", command=salon_trono, width=20)
    boton_opcion.bg = "#FFFFFF"
    boton_opcion.font = "bold"
    app_salir_mazmorra.full_screen = True
    app_salir_mazmorra.display()

def cocina():
    global app_cocina
    app_cocina = App(title="COCINA", width=800, height=600)
    app_cocina.bg = obtener_color_pastel()
    text = Text(app_cocina, text="\nDecides arriesgarte y abrir la puerta derecha. 🚪¡Qué suerte! Es una cocina.", size=14)
    text = Text(app_cocina, text="\nEntras... y... Sorpresa!! está llena de comida recién hecha🍎.", size=14)
    text = Text(app_cocina, text="\n¡Con el hambre que tú tienes, ¡qué bien! 😊.\n", size=14)  
    image = Picture(app_cocina, image="imagenes/cocina.png", width=320, height=240)
    text = Text(app_cocina, text="\n")
    decision_comida_text = Text(app_cocina, text="\n¿Qué haces?\n", size=14)
    decision_box = Box(app_cocina, layout="grid")
    boton_comer = PushButton(decision_box, text="Comer", grid=[0, 0], command=decision_comer, width=20)
    boton_comer.bg = "#FFFFFF"
    boton_comer.font = "bold"
    boton_salir = PushButton(decision_box, text="Salir", grid=[0, 1], command=salir_cocina, width=20)
    boton_salir.bg = "#FFFFFF"
    boton_salir.font = "bold"
    app_cocina.full_screen = True
    app_cocina.display()

def decision_comer():
    app_cocina.hide()
    decision_intoxicacion()

def salir_cocina():
    global app_salir_cocina
    app_salir_cocina = App(title="SALIR COCINA", width=800, height=600)
    app_salir_cocina.bg = obtener_color_pastel()
    text = Text(app_salir_cocina, text="\n Sales de la Cocina por la puerta lateral.... Dónde te llevará 🚪\n", size=14)
    image = Picture(app_salir_cocina, image="imagenes/cocina.png", width=640, height=480)
    text = Text(app_salir_cocina, text="\n")
    boton_continuar = PushButton(app_salir_cocina, text="Continuar", command=jardin, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_salir_cocina.full_screen = True
    app_salir_cocina.display()

def jardin():
    global app_jardin
    app_jardin = App(title="Jardín", width=800, height=600)
    app_jardin.bg = obtener_color_pastel()
    text = Text(app_jardin, text="\nFinalmente y después de algunos sustos 🦇🕸️ en el interior del castillo, 🦇 logras salir y llegas a un bonito jardín... 🦚🌷🌻🌳\n", size=14)
    image = Picture(app_jardin, image="imagenes/jardin.png", width=640, height=480)
    text = Text(app_jardin, text="\n")
    decision_jardin = Text(app_jardin, text="¿Qué haces?\n", size=14)
    decision_box = Box(app_jardin, layout="grid")
    boton_explorar = PushButton(decision_box, text="Explorarlo", grid=[0, 0], command=mazmorra, width=20)
    boton_explorar.bg = "#FFFFFF"
    boton_explorar.font = "bold"
    boton_continuar = PushButton(decision_box, text="Continuar", grid=[0, 1], command=salir_castillo, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_jardin.full_screen = True
    app_jardin.display()

def salon_trono():
    global app_salon_trono
    app_salon_trono = App(title="SALÓN DEL TRONO", width=800, height=600)
    app_salon_trono.bg = obtener_color_pastel()
    text = Text(app_salon_trono, text="\nHas entrado en el salón del trono👑, wow.... , te sientes como una Reina👸\n\nCuando tu seas la 👑, tendrás un trono como este\n", size=14)
    image = Picture(app_salon_trono, image="imagenes/trono.png", width=640, height=480)
    text = Text(app_salon_trono, text="\n")
    decision_salon_trono_text = Text(app_salon_trono, text="¿Qué haces?\n", size=14)
    decision_box = Box(app_salon_trono, layout="grid")
    boton_sentarte = PushButton(app_salon_trono, text="Sentarte", command=mazmorra, width=20)
    boton_sentarte.bg = "#FFFFFF"
    boton_sentarte.font = "bold"
    boton_continuar = PushButton(app_salon_trono, text="Continuar", command=salir_castillo, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_salon_trono.full_screen = True
    app_salon_trono.display()

def habitacion():
    global app_habitacion
    app_habitacion = App(title="HABITACION", width=800, height=600)
    app_habitacion.bg = obtener_color_pastel()
    text = Text(app_habitacion, text="\nWOWWWWW Que bonita habitación 🛏️, la cama parece comoda, estas cansada 💤 después del paseo y las aventuras por el castilo.\n", size=14)
    image = Picture(app_habitacion, image="imagenes/habitacion.png", width=640, height=480)
    text = Text(app_habitacion, text="\n")
    decision_habitacion_text = Text(app_habitacion, text="\n¿Qué haces?\n", size=14)
    decision_box = Box(app_habitacion, layout="grid")
    boton_dormir = PushButton(app_habitacion, text="descansar 💤", command=mazmorra, width=20)
    boton_dormir.bg = "#FFFFFF"
    boton_dormir.font = "bold"
    boton_continuar = PushButton(app_habitacion, text="Continuar", command=salir_castillo, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_habitacion.full_screen = True
    app_habitacion.display()

def decision_intoxicacion():
    global app_intoxicacion
    app_intoxicacion = App(title="INTOXICACIÓN", width=800, height=600)
    app_intoxicacion.bg = obtener_color_pastel()
    text = Text(app_intoxicacion, text="\nTe paras a comer, pero la comida está intoxicada🥒 y te acabas encontrando mal🤢.\n\n💀Esa comida estaba envenenada.", size=14)
    text = Text(app_intoxicacion, text="\nAparece el ratoncito 🐁 para ofrecerte su ayuda.💉 💊🧪\n", size=14)
    image = Picture(app_intoxicacion, image="imagenes/raton.png", width=640, height=480)
    text = Text(app_intoxicacion, text="\n")
    decision_ayuda_text = Text(app_intoxicacion, text="\n¿La aceptas?\n", size=14)
    decision_box = Box(app_intoxicacion, layout="grid")
    boton_si = PushButton(decision_box, text="Sí💉", grid=[0, 0], command=jardin, width=20)
    boton_si.bg = "#FFFFFF"
    boton_si.font = "bold"
    boton_no = PushButton(decision_box, text="No", grid=[1, 0], command=game_over, width=20)
    boton_no.bg = "#FFFFFF"
    boton_no.font = "bold"
    app_intoxicacion.full_screen = True
    app_intoxicacion.display()

def decision_si():
    app_intoxicacion.hide()
    salir_castillo()

def decision_no():
    app_intoxicacion.hide()
    game_over()

def verificar_respuesta(respuesta, app):
    if respuesta.value == "4":
        app.hide()
        salir_castillo()
    else:
        Text(app, text="\n Respuesta incorrecta. Vuelve a intentarlo.")

def game_over():
    #inicio reproducción musica game over
    mixer.init()
    mixer.music.load("mp3/end.mp3")
    mixer.music.play()

    global app_game_over
    app_game_over = App(title="¡FIN!", width=800, height=600)
    app_game_over.bg = obtener_color_pastel()

    text = Text(app_game_over, text="\n¡Deberías haber considerado su ayuda 🐭, acabas muriendo ohhh!!!!!! 🪦☠️", size=14)
    text = Text(app_game_over, text="\nPero...Tienes una nueva oportunidad. 🔄\n", size=14)
    image = Picture(app_game_over, image="imagenes/gameover.png", width=640, height=480)
    text = Text(app_game_over, text="\n")

    #fin reproducción musica game over
    def detener_reproduccion():
        mixer.music.stop()
        mixer.quit()

    def reiniciar_historia():
        detener_reproduccion()
        abrir_inicio()

    boton_inicio = PushButton(app_game_over, text="Nuevo Juego▶️", command=reiniciar_historia, width=20)
    boton_inicio.bg = "#FFFFFF"
    boton_inicio.font = "bold"
    boton_inicio.tk.pack(pady=10)
    boton_cerrar = PushButton(app_game_over, text="Cerrar ⛔", command=sys.exit, width=20)
    boton_cerrar.bg = "#FFFFFF"
    boton_cerrar.font = "bold"
    boton_cerrar.tk.pack(pady=10)
    app_game_over.full_screen = True
    app_game_over.display()

def abrir_inicio():
    mixer.quit()
    subprocess.call(["python", "inicio.py"])
    
def salir_castillo():
    global app_salir_castillo
    app_salir_castillo = App(title="SALIR DEL CASTILLO", width=800, height=600)
    app_salir_castillo.bg = obtener_color_pastel()
    text = Text(app_salir_castillo, text="\nContinúas caminando👣 por el castillo🏰 hasta llegar al exterior... ¡Al fin!", size=14)
    text = Text(app_salir_castillo, text="\n¡Ves a lo lejos a una amable campesina... tiene pinta de buena gente! 👋🌾\n", size=14)
    image = Picture(app_salir_castillo, image="imagenes/salir.png", width=640, height=480)
    text = Text(app_salir_castillo, text="\n")
    boton_continuar = PushButton(app_salir_castillo, text="Continuar", command=campesino, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_salir_castillo.full_screen = True
    app_salir_castillo.display()

def campesino():
    global app_castillo
    app_campesino = App(title="CAMPESINO", width=800, height=600)
    app_campesino.bg = obtener_color_pastel()
    text = Text(app_campesino, text="\n Ella te saluda amablemente👋, tiene una bonita sonrisa😁.", size=14)
    text = Text(app_campesino, text="\n¿Qué haces?\n", size=14)
    image = Picture(app_campesino, image="imagenes/campesino.png", width=640, height=480)
    text = Text(app_campesino, text="\n")
    boton_hablar = PushButton(app_campesino, text="Hablas con ella?", command=hablar_campesino, width=20)
    boton_hablar.bg = "#FFFFFF"
    boton_hablar.font = "bold"
    boton_ignorar = PushButton(app_campesino, text="La Ignoras y continúas", command=ignorar, width=20)
    boton_ignorar.bg = "#FFFFFF"
    boton_ignorar.font = "bold"
    app_campesino.full_screen = True
    app_campesino.display()

def ignorar():
    global app_ignorar
    app_ignorar = App(title="IGNORAR A LA CAMPESINA", width=800, height=600)
    app_ignorar.bg = obtener_color_pastel()
    text = Text(app_ignorar, text="\nDecides ignorar a la campesina 🏰. ¡Ufff!", size=14)
    text = Text(app_ignorar, text="\nTe acuerdas de los guardias... 🫣 pues siguen ahí en el 🏰, no se han ido... 😒\n", size=14)
    image = Picture(app_ignorar, image="imagenes/error.png", width=640, height=480)
    text = Text(app_ignorar, text="\n")
    boton_continuar = PushButton(app_ignorar, text="Continuar", command=mazmorra, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    boton_arrepentir = PushButton(app_ignorar, text="Te arrepientes", command=arrepientes, width=20)
    boton_arrepentir.bg = "#FFFFFF"
    boton_arrepentir.font = "bold"
    app_ignorar.full_screen = True
    app_ignorar.display()

def arrepientes():
    global app_arrepientes
    app_arrepientes = App(title="SEGUNDA OPORTUNIDAD CON LA CAMPESINA")
    app_arrepientes.full_screen = True
    app_arrepientes.bg = obtener_color_pastel()
    text = Text(app_arrepientes, text="\nDecides volver con la campesina🧭. Está ofendida 😡 pero te ofrece el juego de la paz 🕊️🏳️ .\n", size=14)
    image = Picture(app_arrepientes, image="imagenes/ppt.png", width=640, height=480)
    boton_jugar = PushButton(app_arrepientes, text="Jugar", command=jugar_pptijera, width=10, height=2)
    boton_jugar.bg = "#FFFFFF"
    boton_jugar.font = "bold"
    app_arrepientes.display()

def jugar_pptijera():
    app_jugar_pptijera = App(title="II OPORTUNIDAD CON CAMPESINA")
    app_jugar_pptijera.full_screen = True
    app_jugar_pptijera.bg = obtener_color_pastel()

    try:
        # Llamar al programa pptijera.py 
        proceso_pptijera = subprocess.Popen(["python", "pptijera.py"])
        proceso_pptijera.wait()  # Esperar a que el proceso del juego termine

    except Exception as e:
        # Manejar cualquier error al ejecutar pptijera.py
        print("Error al ejecutar pptijera.py:", e)
   
    app_arrepientes.destroy()
    app_jugar_pptijera.destroy()
    wellcome()

def wellcome():
    global app_welcome
    app_welcome = App(title="¡Bienvenida de nuevo!")
    app_welcome.full_screen = True
    app_welcome.bg = obtener_color_pastel()
    mensaje = Text(app_welcome, text="\n\n¡Gracias por volver y jugar!\n\nMe alegra verte...😁\n", size=14, font="bold")
    image = Picture(app_welcome, image="imagenes/campesino.png", width=640, height=480)
    boton_continuar = PushButton(app_welcome, text="Continuar", command=hablar_campesino, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_welcome.display()
    
def hablar_campesino():
    global app_hablar_campesino
    app_hablar_campesino = App(title="HABLAR CON EL CAMPESINO", width=800, height=600)
    app_hablar_campesino.full_screen = True
    app_hablar_campesino.bg = obtener_color_pastel()
    text = Text(app_hablar_campesino, text="\nTen cuidado⚠️, el castillo 🏰 está lleno de peligros ☠️. ¡Sal ASAP del castillo! 🏰", size=14)
    text = Text(app_hablar_campesino, text="\nNo es buena idea💡 permanecer allí mucho tiempo⌛ 🔜.", size=14)
    text = Text(app_hablar_campesino, text="\nSi me ayudas a resolver una pregunta❔, ¿te ayudo a salir? 🆘\n", size=14)
    image = Picture(app_hablar_campesino, image="imagenes/campesino.png", width=640, height=480)
    text = Text(app_hablar_campesino, text="\n")
    boton_continuar = PushButton(app_hablar_campesino, text="Continuar", command=historia, width=20)
    boton_continuar.bg = "#FFFFFF"
    boton_continuar.font = "bold"
    app_hablar_campesino.display()

def historia():
    global app_historia
    app_historia = App(title="Adivina", width=800, height=600)
    app_historia.bg = obtener_color_pastel()
    text = Text (app_historia, text="\nCuál es la capital de Francia París 🥐🗼 o Londres🎡💂.\n", size=14)
    image = Picture(app_historia,image="imagenes/acertijo.png", width=640, height=480)
    text = Text(app_historia, text="\n")
    boton_opcion = PushButton(app_historia, text="Londres",command=historia, width=20)
    boton_opcion.bg = "#FFFFFF"
    boton_opcion.font = "bold"
    boton_opcion = PushButton(app_historia, text="Paris",command=love, width=20)
    boton_opcion.bg = "#FFFFFF"
    boton_opcion.font = "bold"

    app_historia.full_screen = True
    app_historia.display()

def love():
    global app_love
    app_love = App(title="EL PRÍNCIPE", width=800, height=600)
    app_love.bg = obtener_color_pastel()

    text = Text(app_love, text="\nTe encuentras con un príncipe🤴que viene a buscarte en un corcel 🐴.", size=14)
    text = Text(app_love, text="\nTe ofrece irte con él. ¿Qué haces? ¿Te vas con él? 🤔❓\n", size=14)
    image = Picture(app_love, image="imagenes/principe.png", width=640, height=480)
    text = Text(app_love, text="\n")
    boton_Principe = PushButton(app_love, text="Principe", command=final_enamoramiento, width=20)
    boton_Principe.bg = "#FFFFFF"
    boton_Principe.font = "bold"
       
    boton_Sola = PushButton(app_love, text="Sola", command=final_princesa_poderosa, width=20)
    boton_Sola.bg = "#FFFFFF"
    boton_Sola.font = "bold"

    app_love.full_screen = True
    app_love.display()

def final_enamoramiento():

#reproducción musica = para principe 

    mixer.init()
    mixer.music.load("mp3/love.mp3")
    mixer.music.play()

    global app_enamoramiento
    app_enamoramiento = App(title="LOVE", width=800, height=600)
    app_enamoramiento.bg = obtener_color_pastel()

    text = Text(app_enamoramiento, text="\n¡Enhorabuena! Te vas con el príncipe y vives felices para siempre.👸💕🤴\n", size=14)
    image = Picture(app_enamoramiento, image="imagenes/princesayprincipe.png", width=640, height=480)
    text = Text(app_enamoramiento, text="\n")

#detener para no escuchar al reiniciar la historia, se apaga el presionar los botones inicio o cerrar = para principe

    def detener_reproduccion():
        mixer.music.stop()
        mixer.quit()

    def reiniciar_historia():
        detener_reproduccion()
        app_enamoramiento.destroy()
        abrir_inicio()

    boton_inicio = PushButton(app_enamoramiento, text="Volver al inicio", command=reiniciar_historia, width=20)
    boton_inicio.bg = "#FFFFFF"
    boton_inicio.font = "bold"
       
    boton_cerrar = PushButton(app_enamoramiento, text="Cerrar", command=sys.exit, width=20)
    boton_cerrar.bg = "#FFFFFF"
    boton_cerrar.font = "bold"

    app_enamoramiento.full_screen = True
    app_enamoramiento.display()

def final_princesa_poderosa():
    mixer.init()
    mixer.music.load("mp3/brave.mp3")
    mixer.music.play()

    global app_final_princesa_poderosa
    app_princesa_poderosa = App(title="LOVEYOURSELF", width=800, height=600)
    app_princesa_poderosa.bg = obtener_color_pastel()

    text = Text(app_princesa_poderosa, text="\n¡Enhorabuena! 👸💪 Has creado tu propio final. Las princesas no necesitan príncipes tardones⚔️.\n ", size=14)
    image = Picture(app_princesa_poderosa, image="imagenes/princesafin.png", width=640, height=480)
    text = Text(app_princesa_poderosa, text="\n")
    def detener_reproduccion():
        mixer.music.stop()
        mixer.quit()

    def reiniciar_historia():
        detener_reproduccion()
        app_princesa_poderosa.destroy()
        abrir_inicio()

    boton_inicio = PushButton(app_princesa_poderosa, text="Volver al inicio", command=reiniciar_historia, width=20)
    boton_inicio.bg = "#FFFFFF"
    boton_inicio.font = "bold"
       
    boton_cerrar = PushButton(app_princesa_poderosa, text="Cerrar", command=sys.exit, width=20)
    boton_cerrar.bg = "#FFFFFF"
    boton_cerrar.font = "bold"

    app_princesa_poderosa.full_screen = True
    app_princesa_poderosa.display()
          
# Definición tonos pastel predefinida en formato hexadecimal, que aparecerán como fondo de pantalla.(en modo aleatorio)

def obtener_color_pastel():
    colores_pastel = ["#B3D9A0", "#FACF99", "#D7B7A1", "#F7E6AA", "#CFA8A7", "#D6E8C4", "#FCE1B2", "#E9DAC8", "#FCE9C4"]
    return random.choice(colores_pastel)


