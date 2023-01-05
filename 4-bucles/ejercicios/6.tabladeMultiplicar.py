#Ejercicio 6:

#Hacer un programa que pida un nuemero por teclado y guarde en una lista su tabla de multiplicar hasta el 10. 
#Por ejemplo, si digita el 5 la lista tendra: 5,10,15,20,25...

numero = int(input("Digite un numero: "))

lista = []

for i in range(1,11):
    lista.append(i*numero)

print(f"\nTabla de multiplicar: \n{lista}")
