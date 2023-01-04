# Ejercicio 2
# Escriba un programa que tenga dos listas y que, a continuacion, cree las siguientes listas:
# Lista de elementos que aparecen en las dos listas
# Lista de elementos que aparecen en la primera lista, pero no en la segunda
# Lista de elementos que aparecen en la segunda lista, pero no en la primera
# Lista de elementos que aparecen en ambas listas

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

# Eliminar elementos repetidos de ambas listas

a = set(lista1)
b = set(lista2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
interseccion = list (a & b)

print(F"Lista de elementos que aparecen en las dos litas: {union}")
print(f"Lista de elmentos que aparecen en la primer lista, pero no en la segunda: {soloA}")
print(f"Lista de elmentos que aparecen en la segunda lista, pero no en la primera: {soloB}")
print(f"Lista de elementos que aparecen en ambas listas: {interseccion}")