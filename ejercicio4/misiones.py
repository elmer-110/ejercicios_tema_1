from collections import deque

def crear_cola_misiones(misiones):
  
    misiones_ordenadas = sorted(misiones, key=lambda m: m["dificultad"])
    
    cola = deque()
    for mision in misiones_ordenadas:
        cola.append(mision["nombre"])
    
    return cola

misiones = [
    {"nombre": "Rescatar al aldeano", "dificultad": 2},
    {"nombre": "Derrotar al dragón", "dificultad": 5},
    {"nombre": "Recolectar hierbas", "dificultad": 1},
    {"nombre": "Explorar la cueva", "dificultad": 3}
]

cola_misiones = crear_cola_misiones(misiones)

print("Cola de misiones (ordenadas por dificultad):")
for mision in cola_misiones:
    print(f"- {mision}")
