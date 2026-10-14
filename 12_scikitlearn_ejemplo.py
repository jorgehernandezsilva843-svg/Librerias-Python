"""
Ejemplo de uso de la librería 'scikit-learn'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra un flujo completo de Machine Learning (Aprendizaje Automático):
             carga de dataset, división entrenamiento/prueba, entrenamiento de modelo de
             clasificación (Árbol de Decisión), evaluación de métricas y predicción de nuevas muestras.
"""

import sys
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
import numpy as np

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def ejemplo_clasificacion():
    print("\n--- 1. Problema de Clasificación (Dataset Iris con Decision Tree) ---")
    
    # 1. Cargar el dataset clásico de Iris (flores)
    iris = load_iris()
    X = iris.data       # Características: largo/ancho de sépalos y pétalos
    y = iris.target     # Clases objetivo: 0: Setosa, 1: Versicolor, 2: Virginica
    nombres_clases = iris.target_names
    nombres_caracteristicas = iris.feature_names

    print(f"Número de muestras: {X.shape[0]}, Número de características: {X.shape[1]}")
    print(f"Características: {nombres_caracteristicas}")
    print(f"Clases a predecir: {list(nombres_clases)}")

    # 2. Dividir en conjunto de Entrenamiento (80%) y Prueba (20%)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"Muestras de entrenamiento: {len(X_train)} | Muestras de prueba: {len(X_test)}")

    # 3. Instanciar y entrenar el modelo de Clasificación
    modelo_clasificador = DecisionTreeClassifier(max_depth=3, random_state=42)
    modelo_clasificador.fit(X_train, y_train)

    # 4. Evaluación del modelo
    predicciones = modelo_clasificador.predict(X_test)
    exactitud = accuracy_score(y_test, predicciones)
    print(f"\nExactitud (Accuracy) en conjunto de prueba: {exactitud * 100:.2f}%")
    print("\nReporte de clasificación detallado:")
    print(classification_report(y_test, predicciones, target_names=nombres_clases))

    # 5. Predicción con una muestra nueva e hipotética
    # Flor: [longitud sépalo: 5.1, ancho sépalo: 3.5, longitud pétalo: 1.4, ancho pétalo: 0.2]
    nueva_flor = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediccion_nueva = modelo_clasificador.predict(nueva_flor)[0]
    probabilidades = modelo_clasificador.predict_proba(nueva_flor)[0]
    print(f"Muestra nueva {nueva_flor[0]} clasificada como: '{nombres_clases[prediccion_nueva]}'")
    print(f"Probabilidades por clase: {probabilidades}")

def ejemplo_regresion_lineal():
    print("\n--- 2. Problema de Regresión Lineal (Predicción Continua) ---")
    
    # Datos sintéticos: Horas de estudio vs Calificación esperada
    np.random.seed(42)
    horas = np.array([[2], [4], [5], [7], [8], [10], [12], [14], [15], [18]])
    calificaciones = np.array([55, 62, 68, 74, 79, 83, 89, 93, 95, 99])

    # Entrenar regresión lineal
    regresor = LinearRegression()
    regresor.fit(horas, calificaciones)

    # Coeficientes
    pendiente = regresor.coef_[0]
    intercepto = regresor.intercept_
    print(f"Ecuación aprendida: Calificación = ({pendiente:.2f} * Horas) + {intercepto:.2f}")

    # Evaluación R2
    pred_calif = regresor.predict(horas)
    r2 = r2_score(calificaciones, pred_calif)
    print(f"Coeficiente de determinación R²: {r2:.4f}")

    # Predicción: ¿Qué nota sacaría alguien que estudia 11 horas?
    horas_nuevas = np.array([[11]])
    nota_estimada = regresor.predict(horas_nuevas)[0]
    print(f"Predicción para estudiante con 11 horas de estudio: {nota_estimada:.1f} pts")

def main():
    print("=" * 60)
    print("       EJEMPLO DE LA LIBRERÍA: SCIKIT-LEARN")
    print("=" * 60)
    ejemplo_clasificacion()
    ejemplo_regresion_lineal()

if __name__ == "__main__":
    main()
