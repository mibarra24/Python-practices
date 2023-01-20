# Cambio de divisas
# Desarrollar un programa que pueda calcular el valor del tipo
# de cambio de moneda a dolar

def cambio_Pesos_Dolares(pesos):
    return pesos/18.99

def cambio_Dolares_Pesos(dolares):
    return dolares*18.99

while True:
    print("""\t.:MENU:.
1. Convertir Pesos a Dolares
2. Convertir de Dolares a Pesos
3. Salir""")
opcion = int(input("Digite una opcion: "))

print()

if opcion == 1:
    pesos = float(input("Digite la cantidad de pesos: "))
    print(f"Dolares -> ${cambio_Pesos_Dolares(pesos):.2f}")

elif opcion == 2:
    dolares = float(input("Digite la cantidad de dolares: "))
    print(f"Pesos -> ${cambio_Dolares_Pesos(dolares):.2f}")

elif opcion == 3:
    Break

else:
    print("Error")

print()