# trycatch (en python se llama try except)

numberOne, numberTwo = 5, "1"
#numberOne, numberTwo = 5, 1

# try except

try:
    print(numberOne + numberTwo)
except:
    print("Se ha producido un error")

# try except else

try:
    print(numberOne + numberTwo)
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecución continua correctamente")

# try except else finally

try:
    print(numberOne + numberTwo)
except:
    print("Se ha producido un error")
else:
    print("La ejecución continua correctamente")
finally:
    # Se ejecuta pase lo que pase
    print("La ejecución continúa")


# Excepciones por tipo
try:
    print(numberOne + numberTwo)
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información del error
try:
    print(numberOne + numberTwo)
except ValueError as err: # si no es un error de value pasa al Exception
    print(err)
except Exception as err: # esto seria como el clasico catch(err)
    print(err)
