"""
Ejemplo de uso de la librería 'numpy'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra creación de arreglos multidimensionales (ndarrays), operaciones
             vectorizadas, broadcasting, indexación avanzada y cálculo estadístico/matricial.
"""

import numpy as np

def main():
    print("=" * 60)
    print("           EJEMPLO DE LA LIBRERÍA: NUMPY")
    print("=" * 60)

    # 1. Creación de arreglos básicos y propiedades
    print("\n--- 1. Creación de Arreglos y Propiedades ---")
    vector = np.array([10, 20, 30, 40, 50])
    matriz = np.array([[1, 2, 3], [4, 5, 6]])
    
    print(f"Vector 1D: {vector}")
    print(f"Dimensiones (ndim): {vector.ndim}, Forma (shape): {vector.shape}, Tipo (dtype): {vector.dtype}")
    print(f"\nMatriz 2D:\n{matriz}")
    print(f"Dimensiones: {matriz.ndim}, Forma: {matriz.shape}, Total elementos: {matriz.size}")

    # 2. Funciones generadoras de arreglos
    print("\n--- 2. Arreglos Especiales (zeros, ones, arange, linspace) ---")
    ceros = np.zeros((2, 3))
    print(f"Matriz de ceros (2x3):\n{ceros}")

    secuencia = np.arange(0, 20, 5)  # de 0 a 20 con paso de 5
    print(f"Secuencia arange(0, 20, 5): {secuencia}")

    espaciado = np.linspace(0, 1, 5)  # 5 valores equiespaciados entre 0 y 1
    print(f"Lineal linspace(0, 1, 5): {espaciado}")

    # 3. Operaciones vectorizadas (sin bucles for)
    print("\n--- 3. Operaciones Vectorizadas y Broadcasting ---")
    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"Suma elemento a elemento (a + b):  {a + b}")
    print(f"Multiplicación escalar (a * 10):    {a * 10}")
    print(f"Cuadrado de cada elemento (a ** 2): {a ** 2}")

    # 4. Estadísticas descriptivas
    print("\n--- 4. Estadísticas Descriptivas con NumPy ---")
    calificaciones = np.array([85, 90, 78, 92, 88, 76, 95, 89])
    print(f"Datos: {calificaciones}")
    print(f"Media (mean):                   {np.mean(calificaciones):.2f}")
    print(f"Mediana (median):               {np.median(calificaciones):.2f}")
    print(f"Desviación estándar (std):      {np.std(calificaciones):.2f}")
    print(f"Valor mínimo (min):             {np.min(calificaciones)}")
    print(f"Valor máximo (max):             {np.max(calificaciones)}")

    # 5. Filtrado booleano (Máscaras)
    print("\n--- 5. Filtrado Booleano (Masking) ---")
    aprobados = calificaciones[calificaciones >= 80]
    print(f"Calificaciones >= 80:           {aprobados}")

    # 6. Álgebra lineal: Producto punto y transpuesta
    print("\n--- 6. Álgebra Lineal: Multiplicación Matricial ---")
    m1 = np.array([[1, 2], [3, 4]])
    m2 = np.array([[2, 0], [1, 2]])
    producto = np.dot(m1, m2)
    print(f"Matriz M1:\n{m1}")
    print(f"Matriz M2:\n{m2}")
    print(f"Producto matricial (M1 @ M2):\n{producto}")
    print(f"Transpuesta de M1:\n{m1.T}")

if __name__ == "__main__":
    main()
