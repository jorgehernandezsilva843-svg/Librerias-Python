"""
Ejemplo de uso de la librería estándar 'random'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra generación de números pseudoaleatorios, selección de elementos,
             permutaciones, muestreo y reproducibilidad mediante semillas (seed).
"""

import random

def main():
    print("=" * 60)
    print("          EJEMPLO DE LA LIBRERÍA: RANDOM")
    print("=" * 60)

    # 1. Fijar semilla para reproducibilidad (opcional pero muy útil)
    print("\n--- 1. Semilla (Seed) y Números Básicos ---")
    random.seed(42)
    print("Semilla establecida en 42 para resultados reproducibles.")
    print(f"Flotante aleatorio en [0.0, 1.0) (random):   {random.random():.6f}")
    print(f"Flotante aleatorio en rango [5.5, 10.5]:     {random.uniform(5.5, 10.5):.4f}")

    # 2. Enteros aleatorios
    print("\n--- 2. Enteros Aleatorios ---")
    print(f"Entero entre 1 y 10 inclusive (randint):     {random.randint(1, 10)}")
    print(f"Número par entre 10 y 30 con paso 2:         {random.randrange(10, 31, 2)}")

    # 3. Selección en secuencias
    print("\n--- 3. Selección y Muestreo ---")
    frutas = ["Manzana", "Plátano", "Fresa", "Mango", "Uva", "Naranja"]
    print(f"Lista de opciones: {frutas}")
    
    seleccionado = random.choice(frutas)
    print(f"Elemento elegido al azar (choice):          {seleccionado}")

    # choices: con reemplazo (puede repetir elementos)
    con_reemplazo = random.choices(frutas, k=3)
    print(f"3 elecciones con reemplazo (choices):        {con_reemplazo}")

    # sample: sin reemplazo (elementos únicos)
    sin_reemplazo = random.sample(frutas, k=3)
    print(f"3 elecciones sin reemplazo (sample):         {sin_reemplazo}")

    # 4. Barajado / Desordenar listas (in-place)
    print("\n--- 4. Barajar Elementos (Shuffle) ---")
    baraja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Lista original antes de shuffle:            {baraja}")
    random.shuffle(baraja)
    print(f"Lista tras barajar (shuffle):               {baraja}")

    # 5. Ejemplo práctico: Simulación de tirada de dados
    print("\n--- 5. Simulación Práctica: Dos Dados ---")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"Dado 1: {dado1} | Dado 2: {dado2} | Total: {dado1 + dado2}")

if __name__ == "__main__":
    main()
