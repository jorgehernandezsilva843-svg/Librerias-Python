"""
Ejemplo de uso del microframework 'Flask'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra la creación de un servidor web y API REST con rutas estáticas,
             rutas dinámicas con parámetros, recepción de datos JSON y métodos HTTP (GET/POST).
"""

from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Base de datos simulada en memoria
estudiantes_db = [
    {"id": 1, "nombre": "Carlos Gómez", "materia": "Tópicos Avanzados", "calificacion": 95},
    {"id": 2, "nombre": "Ana Morales", "materia": "Bases de Datos", "calificacion": 92},
]

# Plantilla HTML básica para la página de inicio
PAGINA_INICIO_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Servidor Flask - TAP</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background-color: #f7fafc; color: #2d3748; }
        .card { background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 650px; margin: auto; }
        h1 { color: #2b6cb0; }
        code { background-color: #edf2f7; padding: 3px 6px; border-radius: 4px; color: #c53030; }
        ul { line-height: 1.8; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Servidor Web Activo con Flask</h1>
        <p>Demostración para la materia <strong>Tópicos Avanzados de Programación</strong>.</p>
        <h3>Rutas disponibles para probar:</h3>
        <ul>
            <li><code>GET /</code> - Esta página informativa de bienvenida</li>
            <li><code>GET /api/alumnos</code> - Retorna la lista de alumnos en JSON</li>
            <li><code>GET /api/saludo/TuNombre</code> - Saludo dinámico en JSON</li>
            <li><code>GET /api/calculadora?a=10&b=5&operacion=suma</code> - Operaciones matemáticas vía query params</li>
        </ul>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    """Ruta principal que sirve una vista HTML simple."""
    return render_template_string(PAGINA_INICIO_HTML)

@app.route("/api/alumnos", methods=["GET"])
def obtener_alumnos():
    """Retorna la lista de estudiantes en formato JSON."""
    return jsonify({
        "status": "success",
        "total": len(estudiantes_db),
        "data": estudiantes_db
    }), 200

@app.route("/api/alumnos", methods=["POST"])
def agregar_alumno():
    """Agrega un nuevo estudiante a través de un cuerpo JSON."""
    datos = request.get_json()
    if not datos or "nombre" not in datos or "materia" not in datos:
        return jsonify({"status": "error", "message": "Faltan datos obligatorios (nombre, materia)"}), 400

    nuevo_id = len(estudiantes_db) + 1
    nuevo_alumno = {
        "id": nuevo_id,
        "nombre": datos["nombre"],
        "materia": datos["materia"],
        "calificacion": datos.get("calificacion", 0)
    }
    estudiantes_db.append(nuevo_alumno)
    return jsonify({"status": "created", "data": nuevo_alumno}), 201

@app.route("/api/saludo/<string:nombre>", methods=["GET"])
def saludo(nombre):
    """Ruta con parámetro dinámico en la URL."""
    return jsonify({
        "mensaje": f"¡Hola, {nombre}! Bienvenido a la API con Flask.",
        "modulo": "Tópicos Avanzados de Programación"
    })

@app.route("/api/calculadora", methods=["GET"])
def calculadora():
    """Ruta que recibe parámetros de consulta (query parameters)."""
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        operacion = request.args.get("operacion", "suma").lower()

        if operacion == "suma":
            resultado = a + b
        elif operacion == "resta":
            resultado = a - b
        elif operacion == "multiplicacion":
            resultado = a * b
        elif operacion == "division":
            if b == 0:
                return jsonify({"error": "No se puede dividir entre cero"}), 400
            resultado = a / b
        else:
            return jsonify({"error": f"Operación '{operacion}' no soportada"}), 400

        return jsonify({"a": a, "b": b, "operacion": operacion, "resultado": resultado})
    except ValueError:
        return jsonify({"error": "Parámetros 'a' y 'b' deben ser numéricos"}), 400

if __name__ == "__main__":
    print("=" * 60)
    print("           EJEMPLO DEL SERVIDOR: FLASK")
    print("=" * 60)
    print("Iniciando servidor Flask local...")
    print("Abre tu navegador en: http://127.0.0.1:5000")
    # debug=True permite recarga automática en cambios
    app.run(host="127.0.0.1", port=5000, debug=True)
