# Crear un juego con cachipún y un menú de opciones
# La opción número 1 será jugar y la opción 2 salir
import random
# Programar con estructura de control y expresiones boolanas un juego cachipún

print("Bienvenidos al juego del cachipún")
menu_option = 0
while menu_option != 2:
    menu_option = int(input("Ingresa 1 para jugar o 2 para salir: "))
    if menu_option == 1:
        computer_choice = (["piedra","papel","tijeras"])
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
