import random

estadisticas = {
    "modo": None,
    "palabra": "",
    "ganador": "",
    "intentos_usados": 0
}

def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. 1 solo jugador")
    print("2. Ver estadísticas de la última partida")
    print("3. Regresar al menú principal")
    opcion = input("Selecciona una opción: ")
    return opcion

def mostrar_menu_juego():
    print("\n--- MODOS DE JUEGO ---")
    print("1. Contra computadora")
    print("2. Multijugador")
    print("3. Regresar al menú principal")
    return input("Selecciona el modo: ")

def mostrar_estadisticas():
    if estadisticas["modo"]:
        print("\n--- ESTADÍSTICAS DE LA ÚLTIMA PARTIDA ---")
        for clave, valor in estadisticas.items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print("\nNo se han registrado partidas todavía.")

def ocultar_palabra(palabra, letras_adivinadas):
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])

def jugar_1_jugador():
    palabra = random.choice(["computadora", "ahorcado", "python", "teclado", "pantalla"])
    letras_adivinadas = set()
    intentos = 6
    usados = 0

    print("\n¡Comienza el juego del ahorcado!")
    while intentos > 0:
        print("Palabra:", ocultar_palabra(palabra, letras_adivinadas))
        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya usaste esa letra. No se descuentan intentos.")
            continue

        letras_adivinadas.add(letra)
        if letra in palabra:
            print("¡Correcto!")
        else:
            intentos -= 1
            usados += 1
            print(f"Incorrecto. Intentos restantes: {intentos}")

        if all(c in letras_adivinadas for c in palabra):
            print(f"¡Ganaste! La palabra era: {palabra}")
            actualizar_estadisticas("1 jugador", palabra, "Usuario", usados)
            return

    print(f"Perdiste. La palabra era: {palabra}")
    actualizar_estadisticas("1 jugador", palabra, "Computadora", usados)

def jugar_contra_computadora():
    palabra = input("Escribe una palabra para que la computadora la adivine: ").lower()
    letras_usadas = set()
    intentos = 6
    usados = 0
    abecedario = list("abcdefghijklmnopqrstuvwxyz")

    print("\n¡La computadora intentará adivinar tu palabra!")
    while intentos > 0:
        letra = random.choice([l for l in abecedario if l not in letras_usadas])
        letras_usadas.add(letra)
        print(f"La computadora pregunta: ¿La palabra contiene la letra '{letra}'?")
        respuesta = input("Responde 's' o 'n': ").lower()

        if respuesta == 's':
            print("La letra está en la palabra.")
        else:
            intentos -= 1
            usados += 1
            print(f"Incorrecto. Intentos restantes: {intentos}")

        if len(letras_usadas) >= len(set(palabra)):
            break

    ganador = "Computadora" if all(l in letras_usadas for l in set(palabra)) else "Usuario"
    print(f"\nLa palabra era: {palabra}. Ganador: {ganador}")
    actualizar_estadisticas("Contra computadora", palabra, ganador, usados)

def jugar_multijugador():
    palabra = input("Jugador 1, escribe la palabra a adivinar: ").lower()
    letras_adivinadas = set()
    intentos = 6
    usados = 0

    print("\nJugador 2, comienza a adivinar:")
    while intentos > 0:
        print("Palabra:", ocultar_palabra(palabra, letras_adivinadas))
        letra = input("¿La palabra contiene la letra...? ").lower()

        if letra in letras_adivinadas:
            print("Ya la preguntaste.")
            continue

        letras_adivinadas.add(letra)
        if letra in palabra:
            print("¡Correcto!")
        else:
            intentos -= 1
            usados += 1
            print(f"No está. Intentos restantes: {intentos}")

        if all(c in letras_adivinadas for c in palabra):
            print(f"¡Ganaste! La palabra era: {palabra}")
            actualizar_estadisticas("Multijugador", palabra, "Jugador 2", usados)
            return

    print(f"Perdiste. La palabra era: {palabra}")
    actualizar_estadisticas("Multijugador", palabra, "Jugador 1", usados)

def actualizar_estadisticas(modo, palabra, ganador, intentos_usados):
    estadisticas["modo"] = modo
    estadisticas["palabra"] = palabra
    estadisticas["ganador"] = ganador
    estadisticas["intentos_usados"] = intentos_usados

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            modo = mostrar_menu_juego()
            if modo == "1":
                jugar_contra_computadora()
            elif modo == "2":
                jugar_multijugador()
            elif modo == "3":
                continue
            else:
                print("Opción inválida.")
        elif opcion == "2":
            mostrar_estadisticas()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()