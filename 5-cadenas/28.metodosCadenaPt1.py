# Metodos para cadenas

# Cambiar todo a mayuscula

cadena = "Hola mundo".upper()

print(cadena)

# Cambiar todo a minuscula

cadena1 = "Hola mundo".lower()

print(cadena1)

# capitalize: pone mayuscula la primera letra que encuentre

cadena2 = "hola mundo".capitalize()

print(cadena2)

# title: mayusculas las primeras letras de cada palabra

cadena3 = "hola mundo".title()

print(cadena3)

# count: contar caracter indicado

cadena4 = "hola mundo".count('mundo')

print(cadena4)

# find: busca en la cadena el indice de lo que busca

cadena5 = "hola mundo mundo mundo".find('mundo')

print(cadena5)

#rfind: encuentra la ultima coincidencia

cadena6 = "hola mundo mundo mundo".rfind("o")

print(cadena6)

# isdigit: comprueba si existen caracteres numericos o no

cadena7 = "10000".isdigit()

print(cadena7)

# isalpha: comprueba si todos los caracteres son alfabeticos

cadena7 = "Chivas campeon 2023".isalpha()

print(cadena7)

# isalnum: comprueba si hay caracteres alfanumericos

cadena8 = "Chivas campeon 2023".isalnum()

print(cadena8)

# islower: comprueba si toda la cadena esta en minuscula

cadena9 = "hola mundo".islower()

print(cadena9)

# isupper: comprueba si toda la cadena esta en mayuscula

cadena10 = "hola mundo".isupper()

print(cadena10)