import random

# Opciones posibles
opciones = ["Piedra", "Papel", "Tijera"]

# Mensaje de bienvenida
print("Bienvenido al juego de Piedra, Papel o Tijera.")
print("Escribe tu elección: Piedra, Papel o Tijera (o Salir para terminar).")

# Inicialización de puntajes
puntaje_usuario = 0
puntaje_computadora = 0

while True:  # Estructura repetitiva para múltiples rondas
    # Solicitar y validar la elección del usuario
    eleccion_usuario = input("Tu elección: ").strip().capitalize()
    
    if eleccion_usuario == "Salir":  # Si el usuario quiere salir del juego
        print("Gracias por jugar. ¡Hasta luego!")
        break  # Salir del bucle principal
    
    if eleccion_usuario not in opciones:  # Validación de entrada
        print("Entrada no válida. Por favor, elige una opción válida.")
        continue  # Volver al inicio del bucle
    
    # Generar la elección aleatoria de la computadora
    eleccion_computadora = random.choice(opciones)
    print(f"La computadora eligió: {eleccion_computadora}")
    
    # Determinar el resultado del juego
    if eleccion_usuario == eleccion_computadora:
        print("¡Es un empate!")
    elif (eleccion_usuario == "Piedra" and eleccion_computadora == "Tijera") or \
         (eleccion_usuario == "Papel" and eleccion_computadora == "Piedra") or \
         (eleccion_usuario == "Tijera" and eleccion_computadora == "Papel"):
        print("¡Ganaste esta ronda!")
        puntaje_usuario += 1  # Incrementar el puntaje del usuario
    else:
        print("¡Perdiste esta ronda!")
        puntaje_computadora += 1  # Incrementar el puntaje de la computadora
    
    # Mostrar los puntajes acumulados
    print(f"Puntaje: Usuario {puntaje_usuario} - {puntaje_computadora} Computadora\n")