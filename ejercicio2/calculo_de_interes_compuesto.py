
capital_inicial = 1000


tasa_interes_anual = float(input("Introduce la tasa de interés anual (entre 1% y 10%): "))


if tasa_interes_anual < 1 or tasa_interes_anual > 10:
    print("La tasa de interés debe estar entre 1% y 10%.")
else:
  
    numero_anos = int(input("Introduce el número de años: "))

    
    tasa_interes_anual /= 100 
    capital_final = capital_inicial * ((1 + tasa_interes_anual) ** numero_anos)


    print(f"El capital final después de {numero_anos} años es: {capital_final:.2f}")