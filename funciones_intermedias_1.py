# 1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0] = 6  # Cambiar 3 por 6

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"  # Cambiar nombre

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"  # Cambiar Cancún por Monterrey

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431  # Cambiar latitud

# 2. Iterar a través de una lista de diccionarios

def iterarDiccionario(lista):
    for diccionario in lista:
        linea = []
        for clave, valor in diccionario.items():
            linea.append(f"{clave} - {valor}")
        print(", ".join(linea))

# 3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

# 4. Iterar a través de un diccionario con valores de lista

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for valor in lista:
            print(valor)
        print()  # Línea en blanco entre bloques
