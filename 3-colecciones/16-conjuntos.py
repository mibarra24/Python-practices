# Conjuntos

conjunto = set()

conjunto = {1,2,3,"Hola",4.56}

#Agregar elemento a un conjunto
conjunto.add(5)
conjunto.add("Adios")
conjunto.add('a')

# Eliminar elemento de un conjunto
conjunto.discard("Hola")

#Vaciar conjunto
conjunto.clear()

#Buscar elemento
print(3 in conjunto)
print(3 not in conjunto)

print(conjunto)