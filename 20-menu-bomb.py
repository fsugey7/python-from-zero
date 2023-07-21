import time
# Agregar un menú de 2 opciones para ver la bomba de tiempo
# 1 ver bomba de tiempo 2 salir

user_option = 0
while user_option != 2:
    user_option = int(input("Escoge 1 para ver bomba de tiempo o 2 para salir: "))
    if user_option == 1:
        num = 10
        while (num >= 0):
            print(num)
            time.sleep(1)
            num = num - 1
        print("¡¡Boom!!")