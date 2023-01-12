# Ejercicio 3

# Hace un programa que determine si una palabra o frase es palindroma.

cadena = input("Digite una cadena: ")

# Quitar espacio en blanco de la cadena:
cadena = cadena.replace(" ","")
# Invertir la cadena
cadena2 = cadena[::-1]

print(f"La cadena invertida es: {cadena2}")

if cadena == cadena2:
    print("La cadena es un palindromo")
else:
    print("La cadena no es un palindromo")

