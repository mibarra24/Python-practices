# Tuplas: tipo de coleccion parecido a las listas, pero que son inmutables (no se pueden editar o modificar)

tupla = (4,"Hola",6.78,[1,2,3],4)

print(tupla.count(6.78))

print(len(tupla))

#Transformar lista en tupla

list = list(tupla)

print(list)

#Transformar tupla en lista

list = [4,"Hola",6.78,[1,2,3],4]
tupla = tuple(list)

print(tupla)