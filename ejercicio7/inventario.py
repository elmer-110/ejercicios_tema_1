def agregar_item(inventario, item):
    if item in inventario:
        raise ValueError(f"El ítem '{item}' ya está en el inventario.")
    inventario.append(item)

inventario = ["espada", "escudo", "poción"]


agregar_item(inventario, "arco")
print(inventario)  
agregar_item(inventario, "espada")
