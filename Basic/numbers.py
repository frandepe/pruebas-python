# 2 al cubo
print(2**3) # 8
#divisiones...
print(3 / 2) # 1.5
print(3 // 2) # 1
print(3 % 2) # 1 (el residuo)
print(20 - 10 / 5 * 3 **2) # 2.0

#el input toma un caracter de lo que el usuario tipee en la consola

age = input("Inserte su edad: ")
# No podemos sumar un string con un numero, por eso hay que ponerle el tipo numero a age
newAge = int(age) + 5
print(newAge)