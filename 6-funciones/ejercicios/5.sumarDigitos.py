# Ejercicio 5: Sumar digitos con funcion recursiva

'''Desarrollar un programa que permita sumar los digitos de un numero
con ayuda de una funcion recursiva

ejemplo
Entrada = 123
Salida = 6'''

def sumarDigitos(num):
    if num==0:
        resultado = 0
    else:
        resultado = sumarDigitos(int(num/10)) + (num%10)
    
    return resultado

valor = sumarDigitos(123)
print(valor)