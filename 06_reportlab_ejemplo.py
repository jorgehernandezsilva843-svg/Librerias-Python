"""
Ejemplo de uso de la librería 'reportlab'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra la generación de documentos PDF profesionales usando el motor
             Platypus de ReportLab (hojas de estilo, párrafos dinámicos, tablas estilizadas).
"""

import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def generar_pdf_reportlab():
    nombre_archivo = "reporte_reportlab.pdf"
    
    # Configuración del documento
    doc = SimpleDocTemplate(
        nombre_archivo,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    story = []
    estilos = getSampleStyleSheet()

    # Estilos personalizados
    estilo_titulo = ParagraphStyle(
        name="TituloPrincipal",
        parent=estilos["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#1A365D"),
        alignment=1, # Centrado
        spaceAfter=12
    )

    estilo_subtitulo = ParagraphStyle(
        name="Subtitulo",
        parent=estilos["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#4A5568"),
        alignment=1,
        spaceAfter=20
    )

    estilo_cuerpo = ParagraphStyle(
        name="CuerpoTexto",
        parent=estilos["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#2D3748"),
        spaceAfter=10
    )

    # 1. Título y encabezado
    story.append(Paragraph("Instituto Tecnológico - Reporte Ejecutivo", estilo_titulo))
    story.append(Paragraph("Materia: Tópicos Avanzados de Programación | Módulo ReportLab", estilo_subtitulo))
    story.append(Spacer(1, 10))

    # 2. Contenido explicativo
    descripcion = (
        "ReportLab es uno de los paquetes más robustos y estándar de la industria en Python para "
        "la generación programática de documentos PDF complejos. A través de la arquitectura "
        "<b>Platypus</b> (Page Layout and Typography Using Scripts), permite separar el contenido "
        "del diseño de la página de forma declarativa."
    )
    story.append(Paragraph(descripcion, estilo_cuerpo))
    story.append(Spacer(1, 15))

    # 3. Creación de una Tabla estilizada
    datos_tabla = [
        ["Código", "Módulo", "Horas", "Estado"],
        ["TAP-01", "Programación Concurrente", "30 hrs", "Completado"],
        ["TAP-02", "Manipulación de Datos (Pandas)", "40 hrs", "En Curso"],
        ["TAP-03", "Visualización de Gráficos", "25 hrs", "Pendiente"],
        ["TAP-04", "Servicios Web con Flask", "35 hrs", "Pendiente"],
        ["TAP-05", "Aprendizaje Automático (Scikit-Learn)", "45 hrs", "Pendiente"],
    ]

    tabla = Table(datos_tabla, colWidths=[80, 240, 90, 110])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1A365D")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#F7FAFC")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#FFFFFF"), colors.HexColor("#EDF2F7")]),
    ]))

    story.append(tabla)
    story.append(Spacer(1, 20))

    nota_final = "Documento generado automáticamente como evidencia práctica."
    story.append(Paragraph(f"<i>{nota_final}</i>", estilo_cuerpo))

    # Construcción final del PDF
    archivo_final = nombre_archivo
    try:
        doc.build(story)
    except PermissionError:
        archivo_final = "reporte_reportlab_nuevo.pdf"
        doc_alt = SimpleDocTemplate(
            archivo_final,
            pagesize=letter,
            rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40
        )
        doc_alt.build(story)
        print(f"[AVISO DE PERMISOS]: '{nombre_archivo}' está abierto en el visor de PDF.")
        print(f"[OK] Se guardó una copia en: '{archivo_final}'")

    tamano_bytes = os.path.getsize(archivo_final) if os.path.exists(archivo_final) else 0

    # Resumen informativo detallado del PDF en consola
    print(f"\n[OK] Documento PDF generado exitosamente: '{archivo_final}'")
    print("-" * 60)
    print("         INFORMACIÓN DEL ARCHIVO PDF (REPORTLAB)")
    print("-" * 60)
    print(f"Ruta en disco:        {os.path.abspath(archivo_final)}")
    print(f"Tamaño del archivo:   {tamano_bytes / 1024:.2f} KB ({tamano_bytes:,} bytes)")
    print(f"Motor de maquetación: ReportLab Platypus (Flowables)")
    print(f"Dimensiones / Hoja:   Tamaño Carta (Letter: 8.5 x 11 pulgadas)")
    print(f"Márgenes:             40 pt (Izquierdo, Derecho, Superior, Inferior)")
    print(f"Elementos del flujo (Story):")
    print(f"  • Título institucional con ParagraphStyle (Color: #1A365D, Bold 18pt)")
    print(f"  • Subtítulo con estilo Oblique (Color: #4A5568, 11pt)")
    print(f"  • Párrafo de descripción técnica justificada con interlineado leading=14")
    print(f"  • Tabla estilizada con {len(datos_tabla)} filas y {len(datos_tabla[0])} columnas")
    print(f"  • TableStyle con fondo corporativo, texto blanco y filas alternadas")
    print(f"  • Pie de nota final")
    print("-" * 60)
    print("Puedes abrir el archivo generado haciendo doble clic sobre él o ejecutando:")
    print(f"start '{archivo_final}'")

def main():
    print("=" * 60)
    print("         EJEMPLO DE LA LIBRERÍA: REPORTLAB")
    print("=" * 60)
    generar_pdf_reportlab()

if __name__ == "__main__":
    main()
