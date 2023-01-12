# Ejercicio 1

# Hacer un programa donde se debera imprimir por la consola la palabra con mas caracteres de dos palabras dadas
# Mostrar "son iguales" en caso que ambas palabras tengan la misma longitud

cadena1 = input("Digite una cadena: ")
cadena2 = input("Digite otra cadena: ")

if len(cadena1) > len(cadena2):
    print(f"\nLa cadena mas larga es: {cadena1}")
elif len(cadena1) < len(cadena2):
    print(f"\nLa cadena mas larga es: {cadena2}")
else:
    print("\nAmbas cadenas tienen la misma longitud")
