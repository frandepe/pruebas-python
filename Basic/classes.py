# Classes

# pass evita que tengamos que ponerle contenido a una clase y que se ejecute

class EmptyPerson:
    pass

print(EmptyPerson)

# def __init__(self) crea un constructor de clase

class Person:
    def __init__(self, name, surname, age, noName = "Alguien"):
        self.name = name # Propiedad pública
        self.surname = surname
        self.__age = age # Propiedad privada
        self.noName = noName
    def get_name (self):
        return self.__age # Llamamos a la propiedad privada con un metodo
    def walk(self):
        print(f"{self.name} está caminando")

my_person = Person("Franco", "De Paulo", 31)

print(f"{my_person.name} {my_person.surname}")
# print(my_person.__age) # no anda porque es privado
print(my_person.get_name()) 

my_person.walk()