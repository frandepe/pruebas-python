#condicionales: < > == and or not <= >=

x = 20

# el print tiene que ir con un tab para poder validar
if x <= 30:
    print("x es menor que 30")
elif x < 25:
    print("x es menor que 25")
else:
    print("x es mayor que 30")


name = "Jhon"
last_name = "Carter"

# condicional anidada
if name =="Jhon":
    if last_name == "Carter":
        print("Tu eres Jhon Carter")
    else:
        print("Tu no eres Jhon Carter")
else:
    print("Tu no eres Jhon")

# operador logico

if x > 2 and x <= 10:
    print("x es mayor que 2 y menor o igual a 10")
if x > 2 or x <= 20:
    print("x es mayor que 2 y menor o igual a 20")
if (not(x == 50)):
    print("x no es igual a 50")