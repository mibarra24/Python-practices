# Cadenas de caracteres: Indices y slicing

#mostrar caracteres especificos de la cadena

Cadena = "Haaland"

print(Cadena[-1])
print(Cadena[1])

#Slicing

#indiccar que elemento de la cadena va a ser impreso

Cadena1 = "Messi"

print(Cadena1[1:])
print(Cadena1[1:4])

#cadenas son inmutables, no se pueden cambiar elementos directamente
#para cambiarlo se debe hacer lo siguiente:

Cadena2 = "Foden"

Cadena2 = 'f' + Cadena2[1:]

print(Cadena2)

#calcular elementos de la cadena

print(len(Cadena))
print(len(Cadena1))
print(len(Cadena2))