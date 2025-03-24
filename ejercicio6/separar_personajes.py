def separar_personajes(personajes):
    humanos = []
    no_humanos = []

    for personaje in personajes:
        if personaje['tipo'] == 'humano':
            humanos.append(personaje)
        else:
            no_humanos.append(personaje)

    humanos.sort(key=lambda x: x['nombre'])
    no_humanos.sort(key=lambda x: x['nombre'])

    return humanos, no_humanos

# Ejemplo de uso
personajes = [
    {'nombre': 'Mario', 'tipo': 'humano'},
    {'nombre': 'Luigi', 'tipo': 'humano'},
    {'nombre': 'Bowser', 'tipo': 'no humano'},
    {'nombre': 'Yoshi', 'tipo': 'no humano'}
]

humanos, no_humanos = separar_personajes(personajes)
print("Humanos:", humanos)
print("No humanos:", no_humanos)
