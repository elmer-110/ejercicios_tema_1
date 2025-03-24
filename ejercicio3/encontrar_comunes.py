def encontrar_comunes(lista1, lista2):
    diccionario1 = set(lista1)
    diccionario2 = set(lista2)
    
    comunes = diccionario1.intersection(diccionario2)
    
    return list(comunes)

lista1 = ["manzana", "banana", "pera", "manzana"]
lista2 = ["banana", "kiwi", "pera", "pera"]

resultado = encontrar_comunes(lista1, lista2)
print(resultado)