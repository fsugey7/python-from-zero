# Hacer un programa que determine el perímetro de una torta en centímetros.
# Nota para el valor de pi, utilzar 3.14
# El usuario del programa ingresará mediante el teclado el radio de la torta.
cake_radius = int(input("Indica el radio de la torta en centímetros: "))

#Petrímetro de una circuferencia 
# 3.14 * diámetro 
# 3.14 * 2 * radio

perimeter = 2 * 3.13 * cake_radius
print("El perímetro de la torta es", perimeter, "centímetros")