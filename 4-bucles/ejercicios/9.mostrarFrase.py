#Ejercicio 9

# Hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase pero sin espacio en blanco 
#ademas un contador de cuantos caracteres tiuene la drase (sin contar espacios en blanco)
# Ejemplo: Frase: Hola que tal?, frase final: Holaquetal? No de caracteres: 11

frase = input("Digite una frase: ")
frase2 = ""

for i in frase:
    if i!=" ":
        frase2 += i

frase = frase2

print(f"\nFrase final {frase}")
print(f"No. de caracteres: {len(frase)}")