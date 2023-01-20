# Argumentos por valor o por referencia

def doblar_valor(numero):
    numero*= 2
    print(numero)

#Argumento por valor 
n = 5
doblar_valor(n)

print(n)

# Argumento por referencia

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

n = [5,10,15,20]
doblar_valores(n[:])

print(n)