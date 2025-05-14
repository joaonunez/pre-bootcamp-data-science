# ventas_analisis.py

# 1. CARGA DE DATOS
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 1500.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 1450.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 80.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 7, "precio": 20.0},
    {"fecha": "2024-01-03", "producto": "Monitor", "cantidad": 2, "precio": 300.0}
]

print("1. Lista de ventas original:\n")
for v in ventas:
    print(v)

# 2. INGRESOS TOTALES
ingresos_totales = 0
for v in ventas:
    ingresos_totales += v["cantidad"] * v["precio"]

print(f"\n2. Ingresos totales generados: ${ingresos_totales:,.2f}")

# 3. ANÁLISIS DEL PRODUCTO MÁS VENDIDO
ventas_por_producto = {}

for v in ventas:
    producto = v["producto"]
    cantidad = v["cantidad"]
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print(f"\n3. Producto más vendido: {producto_mas_vendido} con {ventas_por_producto[producto_mas_vendido]} unidades")

# 4. PROMEDIO DE PRECIO POR PRODUCTO
precios_por_producto = {}

for v in ventas:
    producto = v["producto"]
    ingreso = v["precio"] * v["cantidad"]
    cantidad = v["cantidad"]

    if producto not in precios_por_producto:
        precios_por_producto[producto] = [0.0, 0]  # [suma precios, total unidades]

    precios_por_producto[producto][0] += ingreso
    precios_por_producto[producto][1] += cantidad

print("\n4. Precio promedio de venta por producto:")
for producto, (total_ingresos, total_unidades) in precios_por_producto.items():
    promedio = total_ingresos / total_unidades
    print(f"- {producto}: ${promedio:.2f}")

# 5. VENTAS POR DÍA
ingresos_por_dia = {}

for v in ventas:
    fecha = v["fecha"]
    ingreso = v["cantidad"] * v["precio"]
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0.0) + ingreso

print("\n5. Ingresos totales por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"- {fecha}: ${ingreso:,.2f}")

# 6. RESUMEN DE VENTAS POR PRODUCTO
resumen_ventas = {}

for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    total_ingresos, total_unidades = precios_por_producto[producto]
    precio_promedio = total_ingresos / total_unidades

    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": total_ingresos,
        "precio_promedio": round(precio_promedio, 2)
    }

print("\n6. Resumen de ventas por producto:")
for producto, datos in resumen_ventas.items():
    print(f"\nProducto: {producto}")
    print(f"  - Cantidad total: {datos['cantidad_total']}")
    print(f"  - Ingresos totales: ${datos['ingresos_totales']:,.2f}")
    print(f"  - Precio promedio: ${datos['precio_promedio']:.2f}")
