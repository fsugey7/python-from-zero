import time
# Python los string ya son varios valores en uno. Cada string está compuesto de caracteres o letras.
some_text = "Algún texto de ejemplo"
# En un texto podemos acceder a cada letra utilizando los [] e indicando su posición partiendo desde 0 
print(some_text[0]) # A
print(some_text[1]) # l
print(some_text[2]) # g

# En Python los string son colecciones de caracyeres. Veremos otras colecciones más adelante, como las listas y los diccionarios
#  Las colecciones las podemos recorrer con el loop for que va a ejecutar su cuerpo una vez por cada elemento de la colección

for letter in some_text:
    print(letter)
for num in range (-10,1):
    print(-1 * num)
    time.sleep(1)
print("Boom")
