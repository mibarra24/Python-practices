# Ejercicio 1
# Escribir la siguiente expresion en formad de expresion algoritmica a3x(b2-2ac)/2b

a = float(input("a -> "))
b = float(input("b -> "))
c = float(input("c -> "))

result = (a**3 * (b**2 - 2*a*c))/(2*b)

print(f"El resultado es: {result}")
