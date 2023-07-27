import pandas as pd


def Escribir(cadena):

    with open("ficha2501234.txt", "w") as plano:
        plano.write(cadena)
    plano.close()


def Leer():
    with open("ficha2501234.txt", "r") as archivo:
        for linea in archivo:
            print(linea)
    archivo.close()


def Actualizar(texto):
    with open("ficha2501234.txt", "+a") as archivo:
        archivo.write("\n")
        archivo.write(texto)
    archivo.close()


# cadena = input("Ingrese un texto: ")
# Escribir(cadena)
# Actualizar(cadena)
# Leer()
