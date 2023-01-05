# Bucle While: Este se evalua una determinada condicion y si es verdadera se sigue ejecutando el bucle hasta que la condicion deje de cumplirse

#Primer ejemplo
import math

numero = int(input("Digite un numero: "))

while numero<0:
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Digite unn numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")

#Segundo ejemplo

i = 0

while i<=10:
    print("Hola mundo")
    i += 1

