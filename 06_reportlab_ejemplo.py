"""
Ejemplo de uso de la librería 'reportlab'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra la generación de documentos PDF profesionales usando el motor
             Platypus de ReportLab (hojas de estilo, párrafos dinámicos, tablas estilizadas).
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

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
    doc.build(story)
    print(f"[OK] Archivo PDF generado exitosamente: '{nombre_archivo}'")

def main():
    print("=" * 60)
    print("         EJEMPLO DE LA LIBRERÍA: REPORTLAB")
    print("=" * 60)
    generar_pdf_reportlab()

if __name__ == "__main__":
    main()
