#Ejercicio 3
#Pide numeros y metelos en una lista, cuando el usuario meta un 0 ya dejamos de insertar. Por ultimo, muestra los numeros ordenados de menos a mayor

list = []

salir = False

while not salir:
    numero = int(input("Digite un numero: "))
    if numero==0:
        salir = True
    else: 
        list.append(numero)

list.sort()

print(f"\nlista ordenada: \n{list}")

