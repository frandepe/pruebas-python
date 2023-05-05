# .txt file
import os

txt_file = open("../my_file.txt", "r+") # Leer y escribir
print(txt_file.read())
print(txt_file.readline())