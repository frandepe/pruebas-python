# nombre = "Franco"
# print(nombre[0:3]) #Fra
# print(nombre[3:]) #nco
# print(nombre[1:3:2]) #r va de 2 en dos del indice 1 al 3
# print(nombre[::-1]) #python entiende que va a ir de uno en uno pero desde el final hacia el principio

# Palindromo

def palindromo(word):
    word = word.replace(" ", "").lower()
    wordInvert = word[::-1]
    if word == wordInvert:
        return True
    else:
        return False
def isPalindromo():
    word = input("Write a word ")
    isPali = palindromo(word)
    if isPali == True:
        print("Is palindromo")
    else:
        print("Is not a palindromo")

# entry point
# esto es el punto de entrada de python, cada vez q encuentra el punto de entrada, corremos la funcion isPalindromo()

if __name__ == '__main__':
    isPalindromo()