from guizero import App, PushButton, Text, TextBox, Box, Picture
import pygame
import Ahorcado as A

def HistoriaCaballero(inicio, personaje):
    inicio.destroy()
    caballero = App(title= "HISTORIA CABALLERO")
    caballero.full_screen = True
    text = Text(caballero, text=f"\nBienvenido estimado {personaje}...")
    text = Text(caballero, text= "La princesa prometida ha sido secuestrada, tu misión será rescatarla de unos malvados guaridas que la tienen encerrada.")
    text = Text(caballero, text= "Para poder ayudarla emprendes un viaje cuando... Te encuentras frente a dos caminos separados por un tronco. Debes decidir qué hacer.\n")
    bosque = Picture(caballero, image= "imagenes/bosqueC.png")
    text = Text(caballero, text= " ")

    def Saltar_Tronco():
        caballero.destroy()
        Corcel()

    def Rodear_Tronco():
        caballero.destroy()
        Troll()

    saltar = PushButton(caballero, text= "Saltar tronco", command= Saltar_Tronco)
    rodear = PushButton(caballero, text= "Rodear tronco", command= Rodear_Tronco)

def Corcel():
    corcel = App(title= "HISTORIA CABALLERO")
    corcel.full_screen = True
    text = Text(corcel, text= "\nSaltas el tronco! Una vez saltado continuas caminando...")
    text = Text(corcel, text= "En el camino, te encuentras con un bonito Corcel.")
    text = Text(corcel, text= "¿Qué haces, difícil decisión no crees?")
    text = Text(corcel, text= "\nQue opción eliges:\n")
    caballo = Picture(corcel, image= "imagenes/corcel.png")
    text = Text(corcel, text= " ")

    def Subir():
        corcel.destroy()
        Campesino()

    def Caminar():
        corcel.destroy()
        Serpiente()

    subir = PushButton(corcel, text= "Subir al corcel", command= Subir)
    caminar = PushButton(corcel, text= "Continuar caminando", command= Caminar)

def Troll():
    troll = App(title= "HISTORIA CABALLERO")
    troll.full_screen = True
    text = Text(troll, text= "\nRodeas el tronco y ves venir un Troll que haces, luchas o huyes?\n")
    trol = Picture(troll, image= "imagenes/troll.png")
    text = Text(troll, text= " ")

    def Luchar():
        troll.destroy()
        Muerte()

    def Huir():
        luchar.destroy()
        huir.destroy()
        text = Text(troll, text= "\nDecides huir y vuelves al camino anterior.\n")
        def Continuar():
            troll.destroy()
            Corcel()
        continuar = PushButton(troll, text= "Continuar", command= Continuar)

    luchar = PushButton(troll, text= "Luchar", command= Luchar)
    huir = PushButton(troll, text= "Huir", command= Huir)

def Muerte():
    muerte = App(title= "HISTORIA CABALLERO")
    muerte.full_screen = True
    pygame.mixer.init()
    pygame.mixer.music.load("mp3/end.mp3")
    pygame.mixer.music.play()
    text = Text(muerte, text= "\nPeleas con el Troll con todas tus fuerzas... pero....")
    text = Text(muerte, text= "El troll te mata... Una verdadera lástima!!!")
    text = Text(muerte, text= "\nDeseas volver a comenzar la aventrua?\n")
    muerto = Picture(muerte, image= "imagenes/game.over.png")
    text = Text(muerte, text= " ")

    def Si():
        muerte.destroy()
        import Inicio

    def No():
        muerte.destroy()

    si = PushButton(muerte, text= "Si", command= Si)
    no = PushButton(muerte, text= "No", command= No)

def Serpiente():
    serpiente = App(title= "HISTORIA CABALLERO")
    serpiente.full_screen = True
    text = Text(serpiente, text= "\nContinúas caminando y de repente... ¡Aparece una serpiente venenosa y te muerde!")
    text = Text(serpiente, text= "La serpiente te ha inyectado su veneno, estás a punto de morir, pero tranquilo...")
    text = Text(serpiente, text= "Puedes obtener un remedio si resuelves este acertijo.")
    text = Text(serpiente, text= "Acertijo: Ponme de lado y soy todo. Córtame por la mitad y no soy nada. ¿Qué número soy?\n") 
    veneno = Picture(serpiente, image= "imagenes/serpiente.png")
    text = Text(serpiente, text= " ")

    def Comprobar_solucion():
        if solucion_acertijo.value == "8":
            serpiente.destroy()
            Corcel1()
        else:
            text.value = ("\nRespuesta incorrecta. Sigue intentando.\n")

    solucion_acertijo = TextBox(serpiente)
    comprobar = PushButton(serpiente, text= "Comprobar", command= Comprobar_solucion)

def Corcel1():
    corcel1 = App(title= "HISTORIA CABALLERO")
    corcel1.full_screen = True
    text = Text(corcel1, text= "\n¡Has acertado el acertijo! Recibes el antídoto, te curas de la mordedura y sigues caminando...")
    text = Text(corcel1, text= "En el camino, te encuentras con un bonito Corcel.")
    text = Text(corcel1, text= "¿Qué haces, difícil decisión no crees?")
    text = Text(corcel1, text= "\nQue opción eliges:\n")
    caballo = Picture(corcel1, image= "imagenes/corcel.png")
    text = Text(corcel1, text= " ")

    def Subir():
        corcel1.destroy()
        Campesino()

    def Caminar():
        corcel1.destroy()
        Serpiente()

    subir = PushButton(corcel1, text= "Subir al corcel", command= Subir)
    caminar = PushButton(corcel1, text= "Continuar caminando", command= Caminar)

def Campesino():
    campesino = App(title= "HISTORIA CABALLERO")
    campesino.full_screen = True
    text = Text(campesino, text= "\nCabalgas en el corcel por el camino hasta que... Llegas al castillo donde te encuentras con un hombre misterioso.")
    text = Text(campesino, text= "El misterioso hombre te ofrece una llave que accede al castillo a cambio de resolver un pequeño acertijo:")
    text = Text(campesino, text= "\n'Cuando tenia 12 años, mi hermana tenia la mitad de mi edad. Ahora que mi hermana tiene 54 años. ¿Cuantos años tengo yo?'\n")
    hobmre = Picture(campesino, image= "imagenes/hmisterioso.png")
    text = Text(campesino, text= " ")

    def Comprobar_solucion():
            if solucion_acertijo.value == "60":
                campesino.destroy() 
                Puerta_Castillo()     
            else:
                text.value = ("\nRespuesta incorrecta. Sigue intentando.\n")

    solucion_acertijo = TextBox(campesino)
    comprobar = PushButton(campesino, text= "Comprobar", command= Comprobar_solucion)

def Puerta_Castillo():
    puerta = App(title= "HISTORIA CABALLERO")
    puerta.full_screen = True

    text = Text(puerta, text= "\n¡Felicidades.... Respuesta correcta! Adelante explora el castillo!!!")   
    text = Text(puerta, text= "Has entrado al castillo y te encuentras con dos puertas. Debes escoger una de ellas.")
    text = Text(puerta, text= "\n¿Que puerta eliges?\n")
    imagen = Picture(puerta, image= "imagenes/2puertas.png")
    text = Text(puerta, text= " ")
    box = Box(puerta, layout="grid")

    def Puerta1():
        puerta.destroy()
        import Laberinto
                    
    def Puerta2():
        puerta.destroy()
        Despensa()

    puerta1 = PushButton(box, image= "imagenes/puerta.png", grid=[0, 0], command= Puerta1)
    puerta2 = PushButton(box, image= "imagenes/puerta.png", grid=[1, 0], command= Puerta2)

def Despensa():
    despensa = App(title= "HISTORIA CABALLERO")
    despensa.full_screen = True
    text = Text(despensa, text= "\n¡Felicidades! Has encontrado la salida del laberinto.")
    text = Text(despensa, text= "Una vez resuelto el laberinto encuentras una salida que te lleva hasta la despensa del castillo.")
    text = Text(despensa, text= "Te encuentras dentro de una enorme despensa, frente a ti tienes una puerta pero a la vez tienes hambre que haces...")
    text = Text(despensa, text= "Tienes tanta hambre que no puedes resistirte y te paras a comer o...")
    text = Text(despensa, text= "Continuas y abres la puerta que hay en la despensa")
    text = Text(despensa, text= "\nQue acción escoges:\n")
    imagen = Picture(despensa, image= "imagenes/despensa.png")
    text = Text(despensa, text= " ")
    
    def Comer():
        despensa.destroy()
        Capturar()
        
    def AbrirPuerta():
        despensa.destroy()
        Abrir_Puerta()

    opcion1 = PushButton(despensa, text= "Comer", command= Comer)
    opcion2 = PushButton(despensa, text= "Abrir puerta", command= AbrirPuerta) 

def Capturar():
    comer = App(title= "HISTORIA CABALLERO")
    comer.full_screen = True
    text = Text(comer, text= "\nA comer... hay ricos manjares sobre las mesas... Mientras comes... te ven los guardias y te capturan.")
    text = Text(comer, text= "Te llevan a la mazmorra junto a la princesa y para salir juntos debéis resolver un acertijo.\n")
    capturado = Picture(comer, image= "imagenes/capturado.png")
    text = Text(comer, text= " ")

    def Continuar():
        comer.destroy()
        Acertijo1() 
    continuar = PushButton(comer, text= "Continuar", command= Continuar)

def Acertijo1():
    acertijo = App(title= "HISTORIA CABALLERO")
    acertijo.full_screen = True
    text = Text(acertijo, text= "\nAcertijo:En la mazmorra, hay tres ladrillos con una letra 'A' dibujada en cada uno.")
    text = Text(acertijo, text= "La llave para liberarte está oculta en uno de los ladrillos. Además, se te proporciona la siguiente información:")
    text = Text(acertijo, text= "El ladrillo 1 se encuentra en la posición contando desde el suelo.")
    text = Text(acertijo, text= "El ladrillo 2 se encuentra en la posición contando desde el techo.")
    text = Text(acertijo, text= "El ladrillo 3 se encuentra en la posición contando desde la esquina derecha de la columna.")
    text = Text(acertijo, text= "Para resolver el acertijo y encontrar la llave, deberás calcular la suma de las posiciones de los tres ladrillos. ¿Cuál es el resultado de esta suma?\n")
    imagen = Picture(acertijo, image= "imagenes/mazmorraC.png")
    text = Text(acertijo, text= " ")

    def Comprobar_solucion():
        if solucion_acertijo.value == "18":
            acertijo.destroy() 
            Final_Juego1()     
        else:
            text.value = ("\nRespuesta incorrecta. Sigue intentando.\n")

    solucion_acertijo = TextBox(acertijo)
    comprobar = PushButton(acertijo, text= "Comprobar", command= Comprobar_solucion)

def Abrir_Puerta():
    abrir = App(title= "HISTORIA CABALLERO")
    abrir.full_screen = True
    text = Text(abrir, text= "\nAbres una de las puertas de la despensa y... Encuentras unas escaleras y un pasillo al fondo.")
    text = Text(abrir, text= "Al final del pasillo esta la mazmorra con la princesa dentro, para liberarla deberás pasar una prueba para encontrar la llave.\n")
    pasillo = Picture(abrir, image= "imagenes/pasillo.png")
    text = Text(abrir, text= " ")

    def Continuar():
        abrir.destroy()
        Acertijo2() 
    continuar = PushButton(abrir, text= "Continuar", command= Continuar)  

def Acertijo2():
    puertas = App(title= "HISTORIA CABALLERO")
    puertas.full_screen = True
    text = Text(puertas, text= "\nLa llave esta dentro en una de las puertas, y tienes 3 puertas delante.")
    text = Text(puertas, text= "La puerta 1 lleva a un ardiente infierno. La puerta 2 a un brutal asesino.")
    text = Text(puertas, text= "Y la puerta 3 a un león que no ha comido en 3 meses.")
    text = Text(puertas, text= "\n¿Qué puerta escoges?\n")
    imagen = Picture(puertas, image= "imagenes/3puertas.png")
    text = Text(puertas, text= " ")
    box = Box(puertas, layout="grid")

    def Puerta_1():
        puertas.destroy()
        Infierno()
    def Puerta_2():
        puertas.destroy()
        Asesino()
    def Puerta_3():
        puertas.destroy()
        Leon()

    puerta1 = PushButton(box, image= "imagenes/puerta.png", grid=[0, 0], command= Puerta_1)
    puerta2 = PushButton(box, image= "imagenes/puerta.png", grid=[1, 0],command= Puerta_2)
    puerta3 = PushButton(box, image= "imagenes/puerta.png", grid=[2, 0],command= Puerta_3)

def Infierno():
    infierno = App(title= "HISTORIA CABALLERO")
    infierno.full_screen = True
    pygame.mixer.init()
    pygame.mixer.music.load("mp3/end.mp3")
    pygame.mixer.music.play()
    text = Text(infierno, text= "\n¡Mala decisión! Has escogido la puerta equivocada.")
    text = Text(infierno, text= "Mueres envuelto entre las llamas del infierno abrasador.\n")
    fuego = Picture(infierno, image= "imagenes/infierno.png")
    text = Text(infierno, text= "\nDeseas volver a comenzar la aventrua?\n")
    text = Text(infierno, text= " ")

    def Si():
        infierno.destroy()
        import Inicio

    def No():
        infierno.destroy()

    si = PushButton(infierno, text= "Si", command= Si)
    no = PushButton(infierno, text= "No", command= No)

def Asesino():
    asesino = App(title= "HISTORIA CABALLERO")
    asesino.full_screen = True
    pygame.mixer.init()
    pygame.mixer.music.load("mp3/end.mp3")
    pygame.mixer.music.play()
    text = Text(asesino, text= "\n¡Mala decisión! Has escogido la puerta equivocada.")
    text = Text(asesino, text= "Eres brutalmente asesinado por un verdugo\n.")
    verdugo = Picture(asesino, image= "imagenes/verdugo.png")
    text = Text(asesino, text= "\nDeseas volver a comenzar la aventrua?\n")
    text = Text(asesino, text= " ")

    def Si():
        asesino.destroy()
        import Inicio

    def No():
        asesino.destroy()

    si = PushButton(asesino, text= "Si", command= Si)
    no = PushButton(asesino, text= "No", command= No)

def Leon():
    leon = App(title= "HISTORIA CABALLERO")
    leon.full_screen = True
    text = Text(leon, text= "\n¡Puerta correcta! El león está muerto tras no comer en 3 meses.")
    text = Text(leon, text= "Coges la llave y te diriges a la mazmorra para liberar a la princesa.\n")
    lion = Picture(leon, image= "imagenes/leon.png")
    text = Text(leon, text= " ")

    def Continuar():
            leon.destroy()
            Final_Juego2()
    continuar = PushButton(leon, text= "Continuar", command= Continuar)

def Final_Juego1():
    final1 = App(title= "HISTORIA CABALLERO")
    final1.full_screen = True
    text = Text(final1, text= "\n¡Has acertado el acertijo! Os liberais y salís hacia el pasillo.")
    text = Text(final1, text= "¡Cuidado! los guardias os persiguen por el castillo.")
    text = Text(final1, text= "Para escapar de ellos debereis superar la siguiente prueba.\n") 
    guardias = Picture(final1, image= "imagenes/guardias.png")
    text = Text(final1, text= " ")

    def Continuar():
            final1.destroy()
            A.Prueba_Final()
    continuar = PushButton(final1, text= "Continuar", command= Continuar)

def Final_Juego2():
    final2 = App(title= "HISTORIA CABALLERO")
    final2.full_screen = True
    text = Text(final2, text= "\nLa liberas y os dirigis a la puerta principal para salir del castillo pero...")
    text = Text(final2, text= "¡Os persiguen los guardias! Para escapar de ellos debereis superar la siguiente prueba.\n")
    guardias = Picture(final2, image= "imagenes/guardias.png")
    text = Text(final2, text= " ")

    def Continuar():
            final2.destroy()
            A.Prueba_Final()
    continuar = PushButton(final2, text= "Continuar", command= Continuar)