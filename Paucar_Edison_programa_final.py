import random

def mostrar_mensaje_bienvenida():
    print("Bienvenido al juego de Piedra, Papel o Tijera.")
    print("Escribe tu elección: Piedra, Papel o Tijera (o Salir para terminar).")

def obtener_eleccion_usuario(opciones):
    while True:
        eleccion = input("Tu elección: ").strip().capitalize()
        if eleccion == "Salir":
            return None
        if eleccion in opciones:
            return eleccion
        print("Entrada no válida. Por favor, elige una opción válida.")

def determinar_resultado(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        return "empate"
    elif (eleccion_usuario == "Piedra" and eleccion_computadora == "Tijera") or \
         (eleccion_usuario == "Papel" and eleccion_computadora == "Piedra") or \
         (eleccion_usuario == "Tijera" and eleccion_computadora == "Papel"):
        return "usuario"
    else:
        return "computadora"

def mostrar_resultado_y_puntaje(resultado, puntajes):
    if resultado == "empate":
        print("¡Es un empate!")
    elif resultado == "usuario":
        print("¡Ganaste esta ronda!")
        puntajes["usuario"] += 1
    else:
        print("¡Perdiste esta ronda!")
        puntajes["computadora"] += 1
    print(f"Puntaje: Usuario {puntajes['usuario']} - {puntajes['computadora']} Computadora\n")

def jugar():
    opciones = ["Piedra", "Papel", "Tijera"]
    puntajes = {"usuario": 0, "computadora": 0}

    mostrar_mensaje_bienvenida()

    while True:
        eleccion_usuario = obtener_eleccion_usuario(opciones)
        if eleccion_usuario is None:
            print("Gracias por jugar. ¡Hasta luego!")
            break

        eleccion_computadora = random.choice(opciones)
        print(f"La computadora eligió: {eleccion_computadora}")

        resultado = determinar_resultado(eleccion_usuario, eleccion_computadora)
        mostrar_resultado_y_puntaje(resultado, puntajes)

if __name__ == "__main__":
    jugar()
