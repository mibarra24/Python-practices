# Funciones con retorno de valor

def multiplicar(num1,num2):
    mult = num1 * num2
    return mult

mult = multiplicar(2,3)

# 2 opciones para imprimirlo

print(mult)

print(multiplicar(2,3))

# retornar varios valores

def prueba():
    return "hola", 45,[1,2,3]

print(prueba())

# Formas de imprimir Cadena, Numero y Lista

c,n,l = prueba()

print(c)
print(n)
print(l)