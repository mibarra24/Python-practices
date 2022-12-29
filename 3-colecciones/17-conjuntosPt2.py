# Conjuntos

a = {1,2,3}
b = {3,4,5}
print(a == b)

c = {2,4,6}
d = {6,4,2}
print(c == d)

#Union de conjuntos
e = a | b
print(e)

#Interseccion de conjuntos
f = a & b
print(f)

#Diferencia de conjuntos
g = a - b
print(g)

#Diferencia simetrica
h = a ^ b
print(h)

#Determinar si un conjunto es subconjunto de otro
i = {1,2,3,4,5}
print(b.issubset(i))

#Conjunto inmutable
j = frozenset({2,7,6})

j.add(3)

print(j)