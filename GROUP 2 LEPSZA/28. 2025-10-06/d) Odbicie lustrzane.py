#d) Odbicie lustrzane (poziome) tej listy, np. dla:

def odbicie(lista):
    for i in range(len(lista)):
        lista[i] = lista[i][::-1]
    return lista
