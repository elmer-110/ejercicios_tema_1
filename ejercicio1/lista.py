def extraer_informacion(cadena_corrupta):
    cadena_invertida = cadena_corrupta[::-1]
    
    partes = cadena_invertida.split(' ')
    nombre_receta = ' '.join(partes[1:])
    calorias = partes[0]

    resultado = f"La receta de {nombre_receta} contiene {calorias} de calorías."
    return resultado

cadena_corrupta = "sáirocal 052 ataceR"
print(extraer_informacion(cadena_corrupta))
