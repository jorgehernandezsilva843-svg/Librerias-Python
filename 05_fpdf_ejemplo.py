"""
Ejemplo de uso de la librería 'fpdf2'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra la creación de documentos PDF, encabezados y pies de página
             personalizados, estilos tipográficos, colores y tablas estructuradas.
"""

import sys
import os
from fpdf import FPDF

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

class PDFReporte(FPDF):
    def header(self):
        # Título institucional
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(30, 60, 114)
        self.cell(0, 10, "Universidad - Tópicos Avanzados de Programación", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 6, "Reporte Generado Automáticamente con FPDF2", border=False, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)
        # Línea divisoria
        self.set_draw_color(30, 60, 114)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(6)

    def footer(self):
        # Posición a 1.5 cm del final
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        # Número de página
        self.cell(0, 10, f"Página {self.page_no()}/{{nb}}", align="C")

def generar_pdf():
    pdf = PDFReporte()
    pdf.add_page()

    # 1. Título principal
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 10, "Reporte de Calificaciones de Alumnos", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    # 2. Párrafo introductorio
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    texto = (
        "El presente informe ha sido construido utilizando la librería FPDF2 para Python. "
        "Permite maquetar documentos PDF con control granular sobre márgenes, fuentes, "
        "colores y elementos tabulares sin requerir utilidades externas."
    )
    pdf.multi_cell(0, 6, texto)
    pdf.ln(5)

    # 3. Construcción de Tabla
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_fill_color(30, 60, 114)
    pdf.set_text_color(255, 255, 255)

    anchos = [30, 60, 55, 35]
    columnas = ["Matrícula", "Nombre Completo", "Materia", "Calificación"]

    # Encabezado de la tabla
    for i, col in enumerate(columnas):
        pdf.cell(anchos[i], 8, col, border=1, align="C", fill=True)
    pdf.ln()

    # Registros
    filas = [
        ("A001", "Carlos Gómez", "Tópicos Avanzados", "95.5"),
        ("A002", "Ana Morales", "Bases de Datos", "92.0"),
        ("A003", "Luis Fernández", "Graficación", "88.5"),
        ("A004", "Beatriz Ramos", "Inteligencia Artificial", "97.0"),
        ("A005", "David Juárez", "Sistemas Distribuidos", "90.0"),
    ]

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(0, 0, 0)
    
    relleno = False
    for fila in filas:
        if relleno:
            pdf.set_fill_color(240, 243, 248)
        else:
            pdf.set_fill_color(255, 255, 255)

        pdf.cell(anchos[0], 7, fila[0], border=1, align="C", fill=True)
        pdf.cell(anchos[1], 7, fila[1], border=1, align="L", fill=True)
        pdf.cell(anchos[2], 7, fila[2], border=1, align="L", fill=True)
        pdf.cell(anchos[3], 7, fila[3], border=1, align="C", fill=True)
        pdf.ln()
        relleno = not relleno

    pdf.ln(5)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, "Total de alumnos registrados: 5 | Estatus: Aprobados", new_x="LMARGIN", new_y="NEXT")

    nombre_salida = "reporte_fpdf.pdf"
    archivo_final = nombre_salida
    try:
        pdf.output(nombre_salida)
    except PermissionError:
        archivo_final = "reporte_fpdf_nuevo.pdf"
        pdf.output(archivo_final)
        print(f"[AVISO DE PERMISOS]: '{nombre_salida}' está abierto en el visor de PDF.")
        print(f"[OK] Se guardó una copia en: '{archivo_final}'")

    tamano_bytes = os.path.getsize(archivo_final) if os.path.exists(archivo_final) else 0

    # Resumen informativo detallado del PDF en consola
    print(f"\n[OK] Documento PDF generado exitosamente: '{archivo_final}'")
    print("-" * 60)
    print("           INFORMACIÓN DEL ARCHIVO PDF (FPDF2)")
    print("-" * 60)
    print(f"Ruta en disco:        {os.path.abspath(archivo_final)}")
    print(f"Tamaño del archivo:   {tamano_bytes / 1024:.2f} KB ({tamano_bytes:,} bytes)")
    print(f"Total de páginas:     {pdf.page_no()}")
    print(f"Formato de página:    A4 vertical (210 x 297 mm)")
    print(f"Motor utilizado:      FPDF2 (Python)")
    print(f"Elementos incluidos:")
    print(f"  • Encabezado institucional personalizado con línea divisoria")
    print(f"  • Párrafo descriptivo con ajuste automático (multi_cell)")
    print(f"  • Tabla de datos con {len(filas)} filas y {len(columnas)} columnas")
    print(f"  • Estilos de celda: encabezado azul marino y filas alternadas tipo cebra")
    print(f"  • Pie de página con paginación dinámica 'Página X/Y'")
    print("-" * 60)
    print("Puedes abrir el archivo generado haciendo doble clic sobre él o ejecutando:")
    print(f"start '{archivo_final}'")

def main():
    print("=" * 60)
    print("           EJEMPLO DE LA LIBRERÍA: FPDF2")
    print("=" * 60)
    generar_pdf()

if __name__ == "__main__":
    main()
