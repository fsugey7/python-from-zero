import random
# Programar con estructura de control y expresiones boolanas un juego cachipún

computer_choice = (["pedra","papel","tijeras"])
print("Bienvenidos al juego del cachipún")
user_option = input(("Escoje entre piedra, papel, tijera: "))


if user_option == computer_choice:
    print("La opción del computador es: ", computer_choice)
    print("¡Empate!")

elif (user_option == "tijera" and computer_choice == "papel") or (user_option == "piedra" and computer_choice == "tijera") or (user_option == "papel" and computer_choice == "piedra"):
    print("La opción del computador es: ", computer_choice)
    print("¡Ganaste!")
else:
    print("La opción del computador es: ", computer_choice)
    print("¡Perdiste!")
