# Ejercicio 1
# Hacer un programa que pida 2 numeros y se de cuenta cual de ellos es par, o si ambos lo son

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

if num1%2==0 and num2%2==0:
    print("Ambos pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par")
else:
    print("Ambos son impares")
