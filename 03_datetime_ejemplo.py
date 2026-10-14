"""
Ejemplo de uso de la librería estándar 'datetime'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra manipulación de fechas, horas, formatos (strftime/strptime),
             operaciones con intervalos de tiempo (timedelta) y diferencias de fechas.
"""

import sys
from datetime import datetime, date, time, timedelta, timezone

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def main():
    print("=" * 60)
    print("         EJEMPLO DE LA LIBRERÍA: DATETIME")
    print("=" * 60)

    # 1. Fecha y hora actual
    ahora = datetime.now()
    hoy = date.today()
    print("\n--- 1. Fechas Actuales ---")
    print(f"Fecha y hora actual completa:        {ahora}")
    print(f"Solo la fecha de hoy:                {hoy}")
    print(f"Año: {ahora.year}, Mes: {ahora.month}, Día: {ahora.day}")
    print(f"Hora: {ahora.hour}, Minutos: {ahora.minute}, Segundos: {ahora.second}")

    # 2. Creación explícita de objetos de fecha y hora
    print("\n--- 2. Creación de Objetos date y time ---")
    fecha_nac = date(2002, 5, 17)
    hora_reunion = time(14, 30, 0)
    evento = datetime(2026, 12, 31, 23, 59, 59)
    print(f"Fecha específica:                    {fecha_nac}")
    print(f"Hora específica:                     {hora_reunion}")
    print(f"Fecha y hora combinada:              {evento}")

    # 3. Formateo de fechas (strftime -> de datetime a cadena legible)
    print("\n--- 3. Formateo de Fechas (strftime) ---")
    formato_es = ahora.strftime("%d/%m/%Y %H:%M:%S")
    formato_largo = ahora.strftime("%A, %d de %B de %Y")
    print(f"Formato estándar DD/MM/AAAA HH:MM:SS: {formato_es}")
    print(f"Formato descriptivo:                  {formato_largo}")

    # 4. Parseo de cadenas a fechas (strptime -> de texto a datetime)
    print("\n--- 4. Parseo de Cadenas (strptime) ---")
    texto_fecha = "2026-10-15 09:30"
    fecha_parseada = datetime.strptime(texto_fecha, "%Y-%m-%d %H:%M")
    print(f"Texto original:                      '{texto_fecha}'")
    print(f"Objeto datetime obtenido:            {repr(fecha_parseada)}")

    # 5. Aritmética de fechas con timedelta
    print("\n--- 5. Operaciones de Tiempo (timedelta) ---")
    plazo_entrega = ahora + timedelta(days=7, hours=3)
    ayer = ahora - timedelta(days=1)
    print(f"Dentro de 7 días y 3 horas será:     {plazo_entrega.strftime('%Y-%m-%d %H:%M')}")
    print(f"Ayer a esta hora era:                 {ayer.strftime('%Y-%m-%d %H:%M')}")

    # 6. Cálculo de diferencia entre fechas
    print("\n--- 6. Diferencia entre dos fechas ---")
    fin_de_ano = datetime(ahora.year, 12, 31)
    diferencia = fin_de_ano - ahora
    print(f"Días restantes para finalizar el año: {diferencia.days} días y {diferencia.seconds // 3600} horas")

if __name__ == "__main__":
    main()
