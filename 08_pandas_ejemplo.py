"""
Ejemplo de uso de la librería 'pandas'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra estructuras Series y DataFrame, filtrado, cálculos de columnas,
             agrupaciones (groupby), resúmenes estadísticos (describe) y exportación de datos.
"""

import sys
import pandas as pd

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def main():
    print("=" * 60)
    print("           EJEMPLO DE LA LIBRERÍA: PANDAS")
    print("=" * 60)

    # 1. Creación de una Serie
    print("\n--- 1. Pandas Series ---")
    edades = pd.Series([21, 22, 20, 23, 21], name="Edad", index=["A1", "A2", "A3", "A4", "A5"])
    print(edades)
    print(f"Edad promedio en la Serie: {edades.mean():.1f} años")

    # 2. Creación de un DataFrame
    print("\n--- 2. Creación de DataFrame ---")
    datos = {
        "Nombre": ["Ana", "Bernardo", "Carlos", "Diana", "Elena", "Fernando", "Gabriela"],
        "Departamento": ["Ventas", "TI", "Ventas", "TI", "RH", "Ventas", "TI"],
        "Salario": [25000, 38000, 27000, 42000, 29000, 26500, 41000],
        "Antiguedad_Anos": [2, 5, 3, 6, 4, 2, 5]
    }
    df = pd.DataFrame(datos)
    print("DataFrame inicial:")
    print(df)

    # 3. Métodos de inspección y estadísticas
    print("\n--- 3. Resumen Estadístico (describe) ---")
    print(df.describe())

    # 4. Creación de columnas calculadas
    print("\n--- 4. Creación de Nuevas Columnas ---")
    # Bono del 10% del salario
    df["Bono"] = df["Salario"] * 0.10
    df["Salario_Total"] = df["Salario"] + df["Bono"]
    print(df[["Nombre", "Salario", "Bono", "Salario_Total"]])

    # 5. Filtrado de datos (condicionales)
    print("\n--- 5. Filtrado de Datos (Salario > 30,000) ---")
    altos_salarios = df[df["Salario"] > 30000]
    print(altos_salarios[["Nombre", "Departamento", "Salario"]])

    # 6. Agrupaciones con GroupBy
    print("\n--- 6. Agrupaciones (groupby por Departamento) ---")
    resumen_depto = df.groupby("Departamento").agg(
        Total_Empleados=("Nombre", "count"),
        Salario_Promedio=("Salario", "mean"),
        Salario_Maximo=("Salario", "max")
    )
    print(resumen_depto)

    # 7. Exportación a CSV
    archivo_csv = "reporte_empleados_pandas.csv"
    try:
        df.to_csv(archivo_csv, index=False, encoding="utf-8")
        print(f"\n[OK] DataFrame exportado correctamente a '{archivo_csv}'")
    except PermissionError:
        archivo_alternativo = "reporte_empleados_pandas_nuevo.csv"
        df.to_csv(archivo_alternativo, index=False, encoding="utf-8")
        print(f"\n[AVISO DE PERMISOS]: No se pudo sobrescribir '{archivo_csv}' porque está abierto en Microsoft Excel u otro visor.")
        print(f"[OK] Se guardó una copia con los datos actualizados en: '{archivo_alternativo}'")
        print("(Consejo: Cierra el archivo en Excel si deseas sobrescribir directamente el original).")

if __name__ == "__main__":
    main()
