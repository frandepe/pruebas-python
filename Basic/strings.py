my_string = "hello world"

#dir nos muestra todos los metodos que le podemos poner a una variable
# print(dir(my_string))
print(my_string.upper())
print(my_string.count("l"))
print(my_string.replace("hello", "bye").swapcase())
print(my_string.startswith("p"))
print(my_string.split("r"))
print(my_string.find("o"))
print(len(my_string))
print(my_string.index("e"))
print(my_string.isnumeric())
print(my_string.isalpha())
print("Mi variable es " + my_string)
print("Mi variable es {0}".format(my_string))
print(my_string[1:4]) #Slice
print(my_string[::-1]) #Reverse

name, surname, age = "Franco", "De Paulo", 31

#Esta es la manera aconsejable de pasar concatenar variables
print("Mi nombre es {} {}, y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s, y mi edad es %d" %(name, surname, age))

#Esta es la mejor forma
print(f"Mi variable es {my_string}")