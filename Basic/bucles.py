# For

foods = ['apples', 'bread', 'milk', 'cheese', 'bananas']

# al llegar a cheese corta con la cadena
# for food in foods:
#     if food == "cheese":
#             break
#     print(food)

# al llegar a cheese lo ignora y continua con lo que sigue
for food in foods:
    if food == "cheese":
            continue
    print(food)

# for number in range(1, 8):
#     print(number)

# for letter in "Hola":
#     print(letter)

# For aplicado a un diccionario y sacando sus valores

cart = {
        "name": "book",
        "price": 4.99,
        "quantity": 3,
    }

for c in cart.values():
    print(c)

# While

count = 4
# Como este while es un if infinito le podemos meter un else
while count <= 10:
    print(count)
    count += 1
    if count == 8:
        print("Se detiene la ejecución")
        break
else: print("La condición terminó")