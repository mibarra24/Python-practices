# Ejercicio 1
# Escriba un programa donde tenga una lista y que, a continuacion, elimine los elementos repetidos, por ultimo, muestra la lista

lista = [1,2,3,"Marco",2,2,1,"Marco",3]

lista = list(set(lista))

print(lista)

