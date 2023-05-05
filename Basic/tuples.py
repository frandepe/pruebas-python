# las tuplas son datos inmutables, no se pueden redefinir
# si le pasamos un solo dato no es considerado una tupla
#en caso de que queramos definir una tupla de un solo elemento le ponemos una , x = (1,)

#estas dos lineas es lo mismo
x = (1, 2, 3)
y = tuple((1,2,3))

# print(dir(x))

# del x # esto elimina la tupla

locations = {
    (35.2133, 39.0000):"Tokyo",
    (23.54433, 40.340):"New York",
}

print(x[-2])