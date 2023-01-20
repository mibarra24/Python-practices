# Funciones sin retorno de valor
# Son un bloque de coquigo dentro de los programas que sirven para resolver problemas especificos, sirven para
# reutilizar el codigo cuantas veces sea necesario, ahorrando tiempo y lineas de codigo.

def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Marco")
saludar("Brenda")

#Tabla de multiplicar de un numero

def tabla_multiplicar(num):
    for i in range(1,11):
        print(f"{num}*{i} = {num*i}")

tabla_multiplicar(2)