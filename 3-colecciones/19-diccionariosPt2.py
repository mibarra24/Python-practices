# Diccionarios Parte 2

equipo = {10:"Alexis Vega",11:"Cone Brizuela",7:"J.J. Macias",17:"Chapo Sanchez"}
# Consultas
# Equipo completo
print(equipo)
# Jugador del dorsal
print(equipo[10])
# Jugardo del dorsal con mensaje si no se encuentra
print(equipo.get(10,"No existe un jugador con ese dorsal"))
# Determinar si hay un dorsal en el equipo
print(12 in equipo)
# Imprimir solo dorsales
print(equipo.keys())
# Cuantos jugadores hay en el equipo
print(len(equipo))