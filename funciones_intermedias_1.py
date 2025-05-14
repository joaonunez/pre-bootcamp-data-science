# funciones_intermedias_1.py

# 1. ACTUALIZAR VALORES EN DICCIONARIOS Y LISTAS
print("1. Actualizar valores en estructuras:")

matriz = [[10, 15, 20], [3, 7, 14]]
print("Matriz original:", matriz)
matriz[1][0] = 6  # Cambiar 3 por 6
print("Matriz actualizada:", matriz)

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
print("\nCantantes original:", cantantes)
cantantes[0]["nombre"] = "Enrique Martin Morales"
print("Cantantes actualizado:", cantantes)

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
print("\nCiudades original:", ciudades)
ciudades["México"][2] = "Monterrey"
print("Ciudades actualizado:", ciudades)

coordenadas = [{"latitud": 8.2588997, "longitud": -84.9399704}]
print("\nCoordenadas original:", coordenadas)
coordenadas[0]["latitud"] = 9.9355431
print("Coordenadas actualizado:", coordenadas)

# 2. ITERAR A TRAVÉS DE UNA LISTA DE DICCIONARIOS
print("\n2. Iterar a través de una lista de diccionarios:")

def iterarDiccionario(lista):
    for diccionario in lista:
        linea = []
        for clave, valor in diccionario.items():
            linea.append(f"{clave} - {valor}")
        print(", ".join(linea))

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

# 3. OBTENER VALORES DE UNA LISTA DE DICCIONARIOS
print("\n3. Obtener valores por clave desde lista de diccionarios:")

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

print("Nombres:")
iterarDiccionario2("nombre", cantantes)

print("\nPaíses:")
iterarDiccionario2("pais", cantantes)

# 4. ITERAR A TRAVÉS DE UN DICCIONARIO CON VALORES DE LISTA
print("\n4. Imprimir información de un diccionario con listas:")

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for valor in lista:
            print(valor)
        print()  # Línea en blanco entre bloques

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)
