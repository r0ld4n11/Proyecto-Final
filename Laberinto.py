import pygame
from guizero import App, Text, PushButton
import Caballero as C

pygame.init()
#Crear las imágenes del juego
class Pared(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laberinto/muro.png").convert()
        self.rect = self.image.get_rect()

class Caballero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laberinto/caballero.png").convert_alpha()
        self.rect = self.image.get_rect()

# Crear los muros y la salida en la ventana
def construir_mapa(mapa):
    listaMuros = []
    x = 0
    y = 0
    for fila in mapa:
        for muro in fila:
            if muro == "X":
                listaMuros.append(pygame.Rect(x, y, 80, 80))
            x += 80
        x = 0
        y += 80
    return listaMuros

def salida(mapa):
    listaMuros = []
    x = 0
    y = 0
    for fila in mapa:
        for muro in fila:
            if muro == "S":
                listaMuros.append(pygame.Rect(x, y, 80, 80))
            x += 80
        x = 0
        y += 80
    return listaMuros

def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, (255, 255, 255), rectangulo)

def Laberinto():
    # Configuración de la pantalla
    ANCHO = 1540
    ALTO = 800
    movil = pygame.Rect(0, 0, 40, 40)
    x = 0
    y = 0
    vel = 0
    alt = 0

    NEGRO = (0, 0, 0)

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Laberinto')
    reloj = pygame.time.Clock()

    listaPared = pygame.sprite.Group()
    pared = Pared()
    listaPared.add(pared)

    listaCaballero = pygame.sprite.Group()
    caballero = Caballero()
    listaCaballero.add(caballero)

    #Reproducir música en el juego
    pygame.mixer.init()
    pygame.mixer.music.load("mp3/Zelda.mp3")
    pygame.mixer.music.play()

    #Dibujar los muros y la salida en la ventana
    mapa = [
            
            " XXXXXXXXXXXXXXXXXXX",
            "  X       X        X",
            "X X X XXXXX XXXXXX X",
            "X X X X   X X    X X",
            "X X X   X X X XX X X",
            "X X XXXXX X X XX X X",
            "X X   X   X X X    X",
            "X XXX X XXX X XXXXXX",
            "X     X     X      S",
            "XXXXXXXXXXXXXXXXXXXX"
    ]

    listaMuros = construir_mapa(mapa)

    Salida = False
    while not Salida:

        reloj.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Salida = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vel = -5
                elif event.key == pygame.K_RIGHT:
                    vel = 5
                elif event.key == pygame.K_UP:
                    alt = -5
                elif event.key == pygame.K_DOWN:
                    alt = 5
            else:
                vel = 0
                alt = 0

        movil.x += vel
        movil.y += alt

        caballero.rect.x = movil.x
        caballero.rect.y = movil.y

        for muro in listaMuros:
            if movil.colliderect(muro):
                movil.x -= vel
                movil.y -= alt

        ventana.fill(NEGRO)

        x = 0
        y = 0
        for fila in mapa:
            for muro in fila:
                if muro == "X":
                    pared.rect.x = x
                    pared.rect.y = y
                    listaPared.add(pared)
                    listaPared.draw(ventana)
                x += 80
            x = 0
            y += 80

        if mapa[movil.y // 80][movil.x // 80] == "S":
            Salida = True
            pygame.quit()
            NuevaVentana()

        listaCaballero.draw(ventana)
        pygame.display.flip()

# Llama a la función Despensa de la parte del Caballero
def NuevaVentana():
    C.Despensa()

Laberinto()