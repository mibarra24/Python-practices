#Ejemplo 7: Juego adivina el numero

#Realiuza un juego para adivinar un numero. Para ello generar un numero aleatorio entre 0-100, y luego ir pidiendo numeros indicando "es mayor" o "es menor" segun sea el caso.
#El proceso termina cuando el usuario acerta y muestra el numero de intentos

#Generamos un numero aleatorio

import random

aleatorio = random.randint(0,100)

print("\t.:Juego adivina el numero: .")

contador = 0
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero>aleatorio:
        print("\tNo es el numero, digita un numero menor")
    elif numero<aleatorio:
        print("\tNo es el numero, digita un numero mayor")
    else:
        print(f"\tFelicidades, acaaba de adivinar el numero {aleatorio}")
        break
    