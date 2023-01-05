#Bucle For: Se utiliza con colecciones. Un iterador recorre elementos de determinada coleccion 

#La variable i recorre elemento por elemento y por eso repite 5 veces el bucle

for i in [1,2,3,4,5]:
    print("Hola mundo")

#De esta forma expresa la cantidad del elemento

for i in [2,10,3,4,"Marco"]:
    print(f"elementro: {i}")

#Formas de ostrar nombre y numero de los futbolistas del FC Barcelona

fcbarcelona = {"Ansu Fati":10,"Ousmane Dembele":11,"Robert Lewandowski":9,"Raphinha":22,"Jules":23,"Marcos Alonso":17,"Pedri":8,"Gavi":30}

for i in fcbarcelona:
    print(f"{i} -> {fcbarcelona[i]}")

for clave,valor in fcbarcelona.items():
    print(f"{clave} -> {valor}")

#Recorrer colecciones

#5 caracteres, separa cada elemento

coleccion = "Marco"

for i in coleccion:
    print(f"{i}")

#quitar salto de linea

for i in coleccion:
    print(f"{i}",end=".")