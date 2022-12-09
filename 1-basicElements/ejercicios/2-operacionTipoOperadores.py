# Ejercicio 2
# Determinar la solucion logica de la siguiente operacion: ((3+5*8)<3 and (((-6/3)*4)+2<2)) or (a>b)

a = float(input("a -> "))
b = float(input("b -> "))

resultado = ((3+5*8)<3 and (-6/3*4)+2<2) or (a>b)

print (f"El resultado es: {resultado}")
