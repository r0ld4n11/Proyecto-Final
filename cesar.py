import tkinter as tk
from tkinter import messagebox
import random
import pygame

def cifrado_cesar(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            if caracter.isupper():
                codigo = ord(caracter) - ord('A')
                codigo = (codigo + desplazamiento) % 26
                caracter_cifrado = chr(codigo + ord('A'))
            else:
                codigo = ord(caracter) - ord('a')
                codigo = (codigo + desplazamiento) % 26
                caracter_cifrado = chr(codigo + ord('a'))
        else:
            caracter_cifrado = caracter
        mensaje_cifrado += caracter_cifrado
    return mensaje_cifrado

def generar_mensaje_cifrado(mensaje, desplazamiento):
    return cifrado_cesar(mensaje, desplazamiento)

def generar_pregunta(mensaje_cifrado):
    desplazamiento = random.randint(1, 25)
    mensaje_oculto = descifrado_cesar(mensaje_cifrado, desplazamiento)
    return mensaje_oculto, desplazamiento

def descifrado_cesar(mensaje_cifrado, desplazamiento):
    mensaje_descifrado = ""
    for caracter in mensaje_cifrado:
        if caracter.isalpha():
            if caracter.isupper():
                codigo = ord(caracter) - ord('A')
                codigo = (codigo - desplazamiento) % 26
                caracter_descifrado = chr(codigo + ord('A'))
            else:
                codigo = ord(caracter) - ord('a')
                codigo = (codigo - desplazamiento) % 26
                caracter_descifrado = chr(codigo + ord('a'))
        else:
            caracter_descifrado = caracter
        mensaje_descifrado += caracter_descifrado
    return mensaje_descifrado

def verificar_respuesta(entry, mensaje_original):
    respuesta = entry.get().upper()
    if respuesta == mensaje_original:
        pygame.mixer.music.load("mp3/puerta.mp3")  # Cargar el archivo de sonido
        pygame.mixer.music.play()  # Reproducir el sonido
        messagebox.showinfo("¡Correcto!", "Has descifrado el mensaje correctamente 👏 👏 👏.")
        ventana.destroy()
    else:
        messagebox.showerror("¡Incorrecto!", "OHHH.. Vuelve a intentarlo😞.")

def jugar_juego():
    global mensaje, ventana

    pygame.mixer.init()  # Inicializar el módulo mixer de pygame
    mensaje = "COMPILADO"  # CAMBIAR EL TEXTO
    mensaje_cifrado = generar_mensaje_cifrado(mensaje, random.randint(1, 25))

    ventana = tk.Tk()
    ventana.title("Juego del Cifrado César")
    ventana.attributes("-fullscreen", True)

    # Cargar la imagen
    imagen = tk.PhotoImage(file="imagenes/cesar.png")
    label = tk.Label(ventana, text="Para poder abrir el castillo deberas resolver...\n\n###CIFRADO CESAR 🤴🏻###,\n\nEste cifrado consiste en sustituir cada letra del abecedario por una letra desplazada un número determinado de posiciones:", font=("Arial", 14))
    label.pack(pady=10)
    label = tk.Label(ventana, text="(TIP)Tenemos varios tipos de lenguajes de interpretación en programación..", font=("Arial", 14), highlightbackground="#BDFCC9")
    label.pack(pady=10)

    mensaje_label = tk.Label(ventana, text=mensaje_cifrado, font=("Arial", 14), highlightbackground="#BDFCC9")
    mensaje_label.pack()

    # Mostrar la imagen
    imagen_label = tk.Label(ventana, image=imagen)
    imagen_label.pack()

    entry = tk.Entry(ventana, font=("Arial", 14))
    entry.pack(pady=10)

    boton = tk.Button(ventana, text="Verificar", command=lambda: verificar_respuesta(entry, mensaje), font=("Arial", 14, "bold"), bg="yellow")
    boton.pack(pady=5)

    ventana.configure(bg="#BDFCC9")  # color de fondo
    ventana.mainloop()

jugar_juego()