"""
Ejemplo de uso de la librería estándar 'csv'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra lectura y escritura de archivos CSV usando tanto listas (writer/reader)
             como diccionarios estructurados (DictWriter/DictReader).
"""

import sys
import csv
import os

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

NOMBRE_ARCHIVO = "estudiantes.csv"

def escribir_csv():
    """Escribe un archivo CSV con cabeceras y registros de alumnos usando DictWriter."""
    estudiantes = [
        {"Matricula": "A001", "Nombre": "Carlos Gómez", "Carrera": "Sistemas", "Promedio": 95.5},
        {"Matricula": "A002", "Nombre": "Ana Morales", "Carrera": "Informática", "Promedio": 92.0},
        {"Matricula": "A003", "Nombre": "Luis Fernández", "Carrera": "Sistemas", "Promedio": 88.5},
        {"Matricula": "A004", "Nombre": "Beatriz Ramos", "Carrera": "Electrónica", "Promedio": 97.0},
    ]

    global NOMBRE_ARCHIVO
    campos = ["Matricula", "Nombre", "Carrera", "Promedio"]

    try:
        with open(NOMBRE_ARCHIVO, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()  # Escribe la fila de títulos de columna
            escritor.writerows(estudiantes)  # Escribe todos los registros
        print(f"[OK] Archivo '{NOMBRE_ARCHIVO}' generado con éxito usando DictWriter.")
    except PermissionError:
        NOMBRE_ARCHIVO = "estudiantes_nuevo.csv"
        with open(NOMBRE_ARCHIVO, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(estudiantes)
        print(f"[AVISO DE PERMISOS]: 'estudiantes.csv' está abierto en Excel u otro programa.")
        print(f"[OK] Se guardó una copia en '{NOMBRE_ARCHIVO}' para continuar la ejecución.")

def leer_csv_estandar():
    """Lee el archivo CSV utilizando csv.reader (acceso por índices numéricos)."""
    print("\n--- Lectura con csv.reader (por lista / índice) ---")
    with open(NOMBRE_ARCHIVO, mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        cabeceras = next(lector)  # Primera fila son las cabeceras
        print(f"Cabeceras detectadas: {cabeceras}")
        for fila in lector:
            matricula, nombre, carrera, promedio = fila
            print(f"Matrícula: {matricula:<5} | Alumno: {nombre:<15} | Carrera: {carrera:<12} | Promedio: {promedio}")

def leer_csv_diccionario():
    """Lee el archivo CSV con csv.DictReader y calcula el promedio general."""
    print("\n--- Lectura con csv.DictReader (por claves de columna) ---")
    suma_promedios = 0.0
    total_alumnos = 0

    with open(NOMBRE_ARCHIVO, mode="r", encoding="utf-8") as archivo:
        lector_dict = csv.DictReader(archivo)
        for fila in lector_dict:
            promedio = float(fila["Promedio"])
            suma_promedios += promedio
            total_alumnos += 1
            print(f"-> {fila['Nombre']} ({fila['Carrera']}) - Nota: {promedio}")

    promedio_general = suma_promedios / total_alumnos if total_alumnos > 0 else 0
    print(f"\nPromedio global de los {total_alumnos} alumnos: {promedio_general:.2f}")

def main():
    print("=" * 60)
    print("           EJEMPLO DE LA LIBRERÍA: CSV")
    print("=" * 60)
    escribir_csv()
    leer_csv_estandar()
    leer_csv_diccionario()

if __name__ == "__main__":
    main()
