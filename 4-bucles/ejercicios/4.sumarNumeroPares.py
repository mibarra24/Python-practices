# Ejercicio 4: Sumar numeros pares dentro de un rango

#Hacer un programa para sumar numero pares dentro de un rango

#Ejemplo: suma de numeros pares del 2 al 30
#suma = 240

a = int(input("Digite de donde va a comenzar a sumar: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))

suma = 0

for i in range(a,b+1):
    if i%2==0: # Si el numero es par
        suma += i

print(f"\nLa suma de numeros pares dentro del rango es: {suma}")

