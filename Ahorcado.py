from guizero import App, Text, PushButton, Picture
import pygame
import random

def Prueba_Final():
    # Configuración de la pantalla
    ANCHO, ALTO = 1540, 800
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)

    # Palabras para adivinar
    palabras = ["python", "programacion", "juego", "ubuntu", "powershell", "interpretado"]

    # Cargar imágenes del ahorcado
    imagenes_ahorcado = []
    for i in range(8):
        imagen = pygame.image.load(f"ahorcado/{i}.png")
        imagenes_ahorcado.append(imagen)

    # Función para seleccionar una palabra aleatoria
    def seleccionar_palabra():
        return random.choice(palabras)

    # Inicializar Pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Juego del Ahorcado")

    # Fuente
    font = pygame.font.SysFont("Arial", 30)

    # Variables del juego
    intentos_maximos = 7
    intentos = 0
    letras_adivinadas = []
    letras_erroneas = []
    palabra_secreta = seleccionar_palabra()

    # Loop principal del juego
    running = True
    while running:
        ventana.fill(BLANCO)

        # Dibujar imagen del ahorcado
        imagen_ahorcado = imagenes_ahorcado[intentos]
        ventana.blit(imagen_ahorcado, (ANCHO // 2 - imagen_ahorcado.get_width() // 2, 50))

        # Dibujar letras adivinadas
        letras_texto = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                letras_texto += letra + " "
            else:
                letras_texto += "_ "
        letras_render = font.render(letras_texto, True, NEGRO)
        ventana.blit(letras_render, (ANCHO // 2 - letras_render.get_width() // 2, 300))

        # Dibujar letras erróneas
        letras_erroneas_texto = "Letras erróneas: " + ", ".join(letras_erroneas)
        letras_erroneas_render = font.render(letras_erroneas_texto, True, NEGRO)
        ventana.blit(letras_erroneas_render, (ANCHO // 2 - letras_erroneas_render.get_width() // 2, 400))

        # Comprobar si el jugador ha ganado
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            resultado_texto = "¡Felicidades! ¡Has ganado!"
            resultado_render = font.render(resultado_texto, True, NEGRO)
            ventana.blit(resultado_render, (ANCHO // 2 - resultado_render.get_width() // 2, 500))
            pygame.display.flip()
            pygame.time.wait(1500)
            running = False
            Ganar()

        # Comprobar si el jugador ha perdido
        if intentos == intentos_maximos:
            resultado_texto = "¡Has perdido! La palabra era: " + palabra_secreta
            resultado_render = font.render(resultado_texto, True, NEGRO)
            ventana.blit(resultado_render, (ANCHO // 2 - resultado_render.get_width() // 2, 500))
            pygame.display.flip()
            pygame.time.wait(1500)
            running = False
            Perder()

        pygame.display.flip()

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letra = chr(event.key)
                    if letra in letras_adivinadas or letra in letras_erroneas:
                        continue
                    if letra in palabra_secreta:
                        letras_adivinadas.append(letra)
                    else:
                        letras_erroneas.append(letra)
                        intentos += 1

def Ganar():
    ganar = App(title="Final")
    ganar.full_screen = True
    pygame.mixer.init()
    pygame.mixer.music.load("mp3/fin.mp3")
    pygame.mixer.music.play()
    text = Text(ganar, text="\n¡Enhorabuena ganaste! Conseguis escapar de los guardias y...")
    text = Text(ganar, text="¡Felicidades! Has conseguido salvar a la pricnesa y completar la aventura con éxito.\n")
    imagen = Picture(ganar, image= "imagenes/finalbueno.png")
    text = Text(ganar, text="\n¿Deseas repetir la aventura?\n")

    def Si():
        pygame.quit()
        ganar.destroy()
        import Inicio

    def No():
        ganar.destroy()

    si = PushButton(ganar, text="Si", command=Si)
    no = PushButton(ganar, text="No", command=No)

    ganar.display()

def Perder():
    perder = App(title="Final")
    perder.full_screen = True
    pygame.mixer.init()
    pygame.mixer.music.load("mp3/end.mp3")
    pygame.mixer.music.play()
    text = Text(perder, text="\n¡Oh no! Es una verdadera lástima pero has perdido")
    text = Text(perder, text="¡No conseguis escapar, os atrapan y os ahorcan a los dos!\n")
    imagen = Picture(perder, image= "imagenes/finalmalo.gif")
    text = Text(perder, text="\n¿Deseas repetir la aventura?\n")

    def Si():
        pygame.quit()
        perder.destroy()
        import Inicio

    def No():
        perder.destroy()

    si = PushButton(perder, text="Si", command=Si)
    no = PushButton(perder, text="No", command=No)
    
    perder.display()