''' Ejercicio 4
Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones aritmeticas basicas. 
El suaurio debe especificar la operacion con el primer caracter del nombre de operacion.

S, s - Suma
R, r - Resta
P, p, M, m - Multiplicacion
D, d - Division
'''

num1 = float(input("Digite un numero: "))
num2 = float(input("Digite un numero: "))

operacion = input("Digite la operacion: ").upper()

if operacion == 'S':
    suma = num1+num2
    print(f"\nLa suma es: {suma}")
elif operacion == 'R':
    resta = num1-num2
    print(f"\nLa resta es: {resta}")
elif operacion == 'M':
    mult = num1*num2
    print(f"\nLa multiplicacion es: {mult}")
elif operacion == 'D':
    div = num1/num2
    print(f"\nLa division es: {div}")
else:
    print("\nSe equivoco de operacion")