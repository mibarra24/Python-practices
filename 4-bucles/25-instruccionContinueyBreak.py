# Instruccion continue y break

#Continue: Cuando llega al 5 continua con lo siguiente

for i in range(10):
    if i==5:
        continue
    print(i)

#Break: corta el proceso hasta antes del 5 y rompe la secuencia

for i in range(10):
    if i==5:
        break
    print(i)
print("Programa finalizado")