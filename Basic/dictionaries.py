from itertools import product

my_dict = dict()

cart = {
        "name": "book",
        "price": 4.99,
        "quantity": 3,
    }

# print(dir(cart))

print(cart.keys())
print(cart.values())
print(cart.items())
print(cart["name"]) #obtener el valor de name
cart["editorial"] = "Penguins" #agregar un campo
del cart["editorial"] # eliminar un campo
print(cart)
print("name" in cart)

# del cart # elimina el diccionario cart
# cart.clear() #vacia el diccionario cart

products = [
    {"name": "book", "price": 10.99},
    {"name": "laptop", "price": 1000}
]

new_dic = dict.fromkeys((1,"name","surname")) # crea un nuevo diccionario sin valores

print(new_dic)