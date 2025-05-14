#ejecutar: en la terminal pip install pandas openpyxl

import os
import pandas as pd

# 1. CARGA DE DATOS
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 1500.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 1450.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 80.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 7, "precio": 20.0},
    {"fecha": "2024-01-03", "producto": "Monitor", "cantidad": 2, "precio": 300.0}
]

# 2. INGRESOS TOTALES
ingresos_totales = sum(v["cantidad"] * v["precio"] for v in ventas)

# 3. ANÁLISIS DEL PRODUCTO MÁS VENDIDO
ventas_por_producto = {}
for v in ventas:
    producto = v["producto"]
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + v["cantidad"]

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

# 4. PROMEDIO DE PRECIO POR PRODUCTO
precios_por_producto = {}
for v in ventas:
    producto = v["producto"]
    ingreso = v["precio"] * v["cantidad"]
    cantidad = v["cantidad"]
    if producto not in precios_por_producto:
        precios_por_producto[producto] = [0.0, 0]
    precios_por_producto[producto][0] += ingreso
    precios_por_producto[producto][1] += cantidad

precios_promedio = {
    producto: round(total_ingresos / total_cantidad, 2)
    for producto, (total_ingresos, total_cantidad) in precios_por_producto.items()
}

# 5. VENTAS POR DÍA
ingresos_por_dia = {}
for v in ventas:
    fecha = v["fecha"]
    ingreso = v["cantidad"] * v["precio"]
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + ingreso

# 6. RESUMEN DE VENTAS
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos, cantidad = precios_por_producto[producto]
    promedio = round(ingresos / cantidad, 2)
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos,
        "precio_promedio": promedio
    }

# 🔽 Crear archivo Excel en el escritorio
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
archivo_excel = os.path.join(desktop, "reporte_ventas.xlsx")

with pd.ExcelWriter(archivo_excel, engine="openpyxl") as writer:
    # Hoja 1 - Ventas originales
    df_ventas = pd.DataFrame(ventas)
    df_ventas.to_excel(writer, sheet_name="Ventas originales", index=False)

    # Hoja 2 - Ingreso total y producto más vendido
    resumen_general = pd.DataFrame([
        {"concepto": "Ingresos Totales", "valor": ingresos_totales},
        {"concepto": "Producto Más Vendido", "valor": producto_mas_vendido},
        {"concepto": "Unidades Vendidas", "valor": ventas_por_producto[producto_mas_vendido]}
    ])
    resumen_general.to_excel(writer, sheet_name="Resumen general", index=False)

    # Hoja 3 - Precio promedio por producto
    df_promedios = pd.DataFrame([
        {"producto": producto, "precio_promedio": promedio}
        for producto, promedio in precios_promedio.items()
    ])
    df_promedios.to_excel(writer, sheet_name="Precio promedio", index=False)

    # Hoja 4 - Ingresos por día
    df_dia = pd.DataFrame([
        {"fecha": fecha, "ingresos_totales": ingreso}
        for fecha, ingreso in ingresos_por_dia.items()
    ])
    df_dia.to_excel(writer, sheet_name="Ingresos por día", index=False)

    # Hoja 5 - Resumen por producto
    df_resumen = pd.DataFrame([
        {
            "producto": producto,
            "cantidad_total": datos["cantidad_total"],
            "ingresos_totales": datos["ingresos_totales"],
            "precio_promedio": datos["precio_promedio"]
        }
        for producto, datos in resumen_ventas.items()
    ])
    df_resumen.to_excel(writer, sheet_name="Resumen por producto", index=False)

print(f"\n✅ Excel generado en el escritorio: {archivo_excel}")
