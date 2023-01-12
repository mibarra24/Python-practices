# Ejercicio 2: Frase terminada en punto
#  Hace un programa que detecte si una frace introducida por el usuario finaliza con un punto o no. 
# La consola debera imprimir: termina con un punto o no termina con un punto

cadena = input("Digite una cadena: ")

if cadena.endswith('.'):
    print("La cadena termina con un punto")
else:
    print("La cadena no finaliza con un punto")



