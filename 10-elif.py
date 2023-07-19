# Podemos encontrar situaciones que se requiere de más de una evaluación condicional para determinar el flujo de ejecución del programa. Esto lo hacemos con la estructura elif que también evalúa una sentencia booleana.

firts_num = int(input("Ingresa el primer número"))
second_num = int(input("Ingresa el segundo número"))

if firts_num > second_num:
    print("El primer número es mayor")
elif firts_num < second_num:
    print("El segundo número es mayor")
else:
    print("Son iguales")