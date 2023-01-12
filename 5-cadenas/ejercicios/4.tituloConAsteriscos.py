# Ejercicio 4:

# Hacer un programa donde se reemplacen todos los espacio de una cadena por asteriscos 
# Cada palabra debe comenzar por mayusculas

cadena = input("Digite una cadena: ")

cadena = cadena.replace(" ","*")

cadena = cadena.title()

print(cadena)