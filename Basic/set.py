# coleccion desordenada sin indice, los valores no se pueden repetir
colors = {'red', "green", "blue"}
more_colors = set({'black', "violet", "yellow", "blue"})

print("red" in colors)
colors.add("pink")
colors.remove("red")
# colors.clear() #limpia todos los elementos
print(colors)
print(more_colors)


union_colors = colors.union(more_colors).union({"sky blue", "brown"})

print(union_colors)
print(union_colors.difference(colors)) # quita de la variable union_colors, los colores de la variable colors