[1, "hello", 1.32, True, [1,2,3]]
colors = ["red", "blue", "green"]
more_colors = ["black", "yellow", "white"]

#constructor

#la tupla agrupa esos cuatro elementos en uno solo,
#lo hacemos asi porq list() solo puede capturar un solo elemento

numbers_list = list((1,2,3,4)) #[1, 2, 3, 4]
print(numbers_list)

#el range() toma dos parametros, de donde a donde quiero crear un elemento

my_rage = list(range(1, 10)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_rage)

my_list = [i * 2 for i in range(8)]
print(my_list)

#dir me muestra la informacion de lo que puedo hacer con una lista (los metodos de javascript)

# print(dir(colors))
# print(len(colors))
# print(colors[-2])
# print("black" in colors)

# como en append se le puede pasar solo un argumento, usamos una tupla
# colors.append(("violet", "black")) # ['red', 'blue', 'green', ('violet', 'black')]
# colors.extend(("violet", "black")) # ['red', 'blue', 'green', 'violet', 'black']
# colors.extend(["brown", "yellow"]) # ['red', 'blue', 'green', 'violet', 'black', 'brown', 'yellow']
# colors.insert(1, "violet")
# colors.pop() # elimina el ultimo
# colors.remove("green") # elimina solo el primer elemento
# colors.pop(1) # quita el indice 1
# colors.clear() # deja la lista vacia
# del colors(2) # elimina el indice 2

# print(colors[1:3]) # me muestra los colores q hay entre el indice 1 y 3

#ordenar una lista

# colors.sort()
# colors.sort(reverse=True)

#contar elementos

# colors.count("red")

# print(colors + more_colors) # concatena las listas

print(colors)