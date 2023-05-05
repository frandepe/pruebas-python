# modulo que podemos escribir nosotros mismos
# modulos de bibliotecas de terceros
# modulos que nos da python

#modulo de python:
# podemos googlear python modules
#en google pipe modules para buscar los mas utilizador por la comunidad

# import datetime
# tambien se puede importar asi para no repetir datetime.algo
from datetime import timedelta, date
#importamos el archivo fmath.py
import fmath
# from fmath import add, substract

print(date.today())
#convierte minutos a horas # 1:10:00
print(timedelta(minutes=70))

fmath.add(1,2)
fmath.substract(1,2)

# pypi.org - web para librerias
# para instalar una libreria pip install

from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + "Hello World")