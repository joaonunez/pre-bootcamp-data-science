# 1. Básico: imprime todos los números enteros del 0 al 100.
print("1. Básico:")
for i in range(0, 101):
    print(i)

# 2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
print("\n2. Múltiples de 2:")
for i in range(2, 501, 2):
    print(i)

# 3. Contando Vanilla Ice: imprime los números del 1 al 100.
# Si es divisible por 5, imprime "ice ice", si es divisible por 10, imprime "baby"
print("\n3. Contando Vanilla Ice:")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# 4. Wow. Número gigante a la vista: suma los números pares del 0 al 500,000
print("\n4. Wow. Número gigante a la vista:")
suma = 0
for i in range(0, 500001, 2):
    suma += i
print("Suma total:", suma)

# 5. Regrésame al 3: cuenta regresivamente desde 2024 en pasos de 3
print("\n5. Regrésame al 3:")
for i in range(2024, 0, -3):
    print(i)

# 6. Contador dinámico
print("\n6. Contador dinámico:")
numInicial = 3
numFinal = 10
multiplo = 2
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
