from guizero import App, Box, PushButton, Text, Picture
import random

# Función para determinar quién gana.
def determinar_ganador(opcion_usuario, opcion_maquina):
    if opcion_usuario == opcion_maquina:
        return "Empate"
    elif (opcion_usuario == "Piedra" and opcion_maquina == "Tijera") or \
         (opcion_usuario == "Papel" and opcion_maquina == "Piedra") or \
         (opcion_usuario == "Tijera" and opcion_maquina == "Papel"):
        return "Ganaste"
    else:
        return "Perdiste"

# Función para generar los botones
def clic(opcion):
    opciones = ["Piedra", "Papel", "Tijera"]
    opcion_maquina = random.choice(opciones)
    resultado = determinar_ganador(opcion, opcion_maquina)
    etiqueta_resultado.value = f"Tú elegiste: {opcion}\nLa máquina eligió: {opcion_maquina}\nResultado: {resultado}"
    if resultado == "Ganaste":
        etiqueta_resultado.bg = "green"
        app.destroy()  # Cerrar la aplicación cuando el jugador gana
    elif resultado == "Perdiste":
        etiqueta_resultado.bg = "red"
    else:
        etiqueta_resultado.bg = "yellow"

# Colores pastel, asignacion finales fondo.
colores_pastel = ["#FADBD8", "#D2E9F7", "#F9E79F", "#F5D5E3", "#D4EFDF", "#FDEBD0"]

# Crear la aplicación
app = App("Piedra, Papel, Tijera", width=640, height=600, bg="lightblue")

caja = Box(app, layout="grid")
etiqueta_elegir = Text(caja, text="\nSabes cómo se juega a piedra, papel, tijera?\n\nSelecciona tu opción:\n", grid=[0, 0, 3, 1], size=14, color="black")
imagen_ppt = Picture(caja, image="ppt.gif", grid=[0, 1, 3, 1], width=640, height=480)  # Ruta al archivo GIF
boton_piedra = PushButton(caja, text="Piedra", command=clic, args=["Piedra"], grid=[0, 2], width=8, height=2)
boton_piedra.bg = random.choice(colores_pastel)
boton_papel = PushButton(caja, text="Papel", command=clic, args=["Papel"], grid=[1, 2], width=8, height=2)
boton_papel.bg = random.choice(colores_pastel)
boton_tijera = PushButton(caja, text="Tijera", command=clic, args=["Tijera"], grid=[2, 2], width=8, height=2)
boton_tijera.bg = random.choice(colores_pastel)
etiqueta_resultado = Text(caja, text="", grid=[0, 3, 3, 1], size=14, color="black")

# Centrar los botones en medio de la pantalla
caja.tk.pack_configure(pady=20)

# Ejecutar la aplicación
app.display()
