 

def conver(pais, moneda):
    pesos = input("¿Cuantos pesos " + pais + " tenes?: ")
    pesos = float(pesos)
    valor_dolar = moneda
    dolares = pesos / valor_dolar
    doalres = round(dolares, 2)
    dolares = str(dolares)
    print("Tenes " + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 😉

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: 
"""
opcion = input(menu)

if opcion == '1':
    conver("colombianos", 3800)
elif opcion == '2':
    conver("argentinos", 320)
elif opcion == '3':
    conver("mexicanos", 40)
else:
    print("Ingresa una opción correcta")

