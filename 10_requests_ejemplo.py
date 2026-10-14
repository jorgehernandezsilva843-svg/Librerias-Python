"""
Ejemplo de uso de la librería 'requests'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra peticiones HTTP (GET, POST), manejo de cabeceras (headers),
             parámetros de consulta (query params), serialización JSON y códigos de estado.
"""

import requests
import urllib3

# Deshabilitar advertencias de certificados no verificados en caso de proxies o entornos locales
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def hacer_peticion(metodo, url, **kwargs):
    """Función auxiliar que intenta con verificación SSL y respaldo sin verificación."""
    try:
        return metodo(url, timeout=6, **kwargs)
    except requests.exceptions.SSLError:
        return metodo(url, verify=False, timeout=6, **kwargs)

def peticion_get():
    """Ejemplo de petición GET consumiendo una API REST pública (JSONPlaceholder)."""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    print(f"Enviando GET a: {url}")

    try:
        respuesta = hacer_peticion(requests.get, url)
        print(f"Código de estado HTTP: {respuesta.status_code}")
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            print("\nDatos recibidos (JSON deserializado a dict):")
            print(f"ID del Post: {datos.get('id')}")
            print(f"Título:      {datos.get('title')}")
            print(f"Cuerpo:      {datos.get('body')}")
        else:
            print(f"Error en la petición: {respuesta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Nota: No se pudo conectar al servicio externo: {e}")

def peticion_post():
    """Ejemplo de petición POST enviando datos en formato JSON."""
    url = "https://jsonplaceholder.typicode.com/posts"
    nuevo_post = {
        "title": "Práctica de Tópicos Avanzados de Programación",
        "body": "Demostración de envío de cargas útiles (payloads) con requests.",
        "userId": 42
    }
    encabezados = {
        "Content-type": "application/json; charset=UTF-8"
    }

    print(f"\nEnviando POST a: {url}")
    try:
        respuesta = hacer_peticion(requests.post, url, json=nuevo_post, headers=encabezados)
        print(f"Código de estado HTTP: {respuesta.status_code} (201 = Created)")
        print(f"Respuesta del servidor con el recurso creado:\n{respuesta.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Nota: No se pudo conectar al servicio externo: {e}")

def peticion_con_parametros():
    """Ejemplo de GET con parámetros de consulta (?param=valor)."""
    url = "https://jsonplaceholder.typicode.com/comments"
    parametros = {"postId": 1}

    print(f"\nConsultando comentarios del postId=1 con query parameters...")
    try:
        respuesta = hacer_peticion(requests.get, url, params=parametros)
        comentarios = respuesta.json()
        print(f"Se recibieron {len(comentarios)} comentarios:")
        for c in comentarios[:3]:  # mostramos los 3 primeros
            print(f"- De: {c.get('email')} | Asunto: {c.get('name')[:30]}...")
    except requests.exceptions.RequestException as e:
        print(f"Nota: No se pudo conectar al servicio externo: {e}")

def main():
    print("=" * 60)
    print("         EJEMPLO DE LA LIBRERÍA: REQUESTS")
    print("=" * 60)
    peticion_get()
    peticion_post()
    peticion_con_parametros()

if __name__ == "__main__":
    main()
