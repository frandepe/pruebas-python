# name="Persona" crea un valor por defecto, pasa lo mismo en JS

def miFunctionHello(name="Persona"):
    print("hello " + name)

miFunctionHello("joe")

def addFunction(num1, num2):
    return num1 + num2

print(addFunction(30, 10))

#funcion lambda, una funcion que no tiene nombre con dos parametros que retorna algo
#lambda es una funcion anónima
add = lambda numOne, numTwo: numOne + numTwo
print(add(10, 20))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))

### Higher order functions (funciones de orden superior) ###
# Funciones que son capaces de ejecutar funciones

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_one(5, 2, sum_one))
print(sum_two_values_and_add_one(5, 2, sum_five))

### Closure ###
#Funcion que retorna otra funcion

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(5)
print(add_closure(5))

#Lo podemos invocar como una lambda
print(sum_ten(5)(1))

### Built-in Higher order function ###

numbers = [2,5,17,23]

# Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter

print(list(filter(lambda number: number > 10, numbers)))

# Reduce
import functools
print(functools.reduce(lambda a, b: a + b, numbers))