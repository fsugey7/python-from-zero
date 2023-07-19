# Una evalucaión condicional puede estar dentro de otra:

name = input("Hola, Cuál es tu nombre?")
age = int(input("Dime tu edad"))

if age >= 18:
    drink = input("¿Quieres cerveza o vino?")
    print("Toma" ,name)
    if drink == "cerveza":
        print("Aqui tienes tu cerveza")
    else:
        print("Aqui está tu vino")
else:
    juice = input("¿Quieres jugo de frutilla o naranja?")
    print("Toma",name)
    if juice == "frutilla":
        print("Aqui tienes tu jugo de frutilla")
    else:
        print("Awui tienes tu jugo de naranja")