"""
Ejemplo de uso de la librería 'matplotlib'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra visualización gráfica: gráfico de líneas, gráfico de barras,
             diagrama de dispersión e histograma dentro de una figura multipanel (subplots).
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def generar_graficas():
    # Creamos una figura con una cuadrícula de 2x2 subgráficos
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle("Demostración de Tipos de Gráficas con Matplotlib", fontsize=16, fontweight="bold")

    # 1. Gráfico de Líneas (ax[0, 0])
    x = np.linspace(0, 10, 100)
    y_seno = np.sin(x)
    y_coseno = np.cos(x)
    axs[0, 0].plot(x, y_seno, label="Seno(x)", color="navy", linewidth=2)
    axs[0, 0].plot(x, y_coseno, label="Coseno(x)", color="crimson", linestyle="--", linewidth=2)
    axs[0, 0].set_title("1. Gráfico de Líneas (Funciones Trigonométricas)")
    axs[0, 0].set_xlabel("Eje X (Radianes)")
    axs[0, 0].set_ylabel("Amplitud")
    axs[0, 0].grid(True, linestyle=":", alpha=0.6)
    axs[0, 0].legend()

    # 2. Gráfico de Barras (ax[0, 1])
    lenguajes = ["Python", "Java", "C++", "C#", "JavaScript"]
    popularidad = [90, 75, 60, 68, 85]
    colores_barras = ["#3B82F6", "#EF4444", "#10B981", "#8B5CF6", "#F59E0B"]
    barras = axs[0, 1].bar(lenguajes, popularidad, color=colores_barras, edgecolor="black")
    axs[0, 1].set_title("2. Gráfico de Barras (Índice de Popularidad)")
    axs[0, 1].set_ylabel("Puntaje / 100")
    axs[0, 1].set_ylim(0, 105)
    for bar in barras:
        yval = bar.get_height()
        axs[0, 1].text(bar.get_x() + bar.get_width()/2, yval + 2, f"{yval}%", ha="center", fontsize=9)

    # 3. Diagrama de Dispersión / Scatter (ax[1, 0])
    np.random.seed(42)
    horas_estudio = np.random.uniform(2, 20, 30)
    calificacion = np.clip(horas_estudio * 3.8 + np.random.normal(20, 5, 30), 0, 100)
    axs[1, 0].scatter(horas_estudio, calificacion, color="purple", alpha=0.7, edgecolors="black", s=60)
    axs[1, 0].set_title("3. Dispersión: Horas de Estudio vs Calificación")
    axs[1, 0].set_xlabel("Horas semanales dedicadas")
    axs[1, 0].set_ylabel("Calificación obtenida")
    axs[1, 0].grid(True, linestyle="--", alpha=0.5)

    # 4. Histograma (ax[1, 1])
    datos_normales = np.random.normal(loc=75, scale=10, size=250)
    axs[1, 1].hist(datos_normales, bins=15, color="#059669", edgecolor="white", alpha=0.85)
    axs[1, 1].set_title("4. Histograma de Distribución de Notas")
    axs[1, 1].set_xlabel("Rangos de Calificación")
    axs[1, 1].set_ylabel("Frecuencia de Alumnos")
    axs[1, 1].grid(axis="y", linestyle=":", alpha=0.6)

    plt.tight_layout()

    nombre_salida = "graficas_matplotlib.png"
    try:
        plt.savefig(nombre_salida, dpi=300)
        print(f"[OK] Gráfica guardada como imagen en: '{nombre_salida}'")
    except PermissionError:
        nombre_alternativo = "graficas_matplotlib_nueva.png"
        plt.savefig(nombre_alternativo, dpi=300)
        print(f"[AVISO DE PERMISOS]: '{nombre_salida}' está abierta en el visor.")
        print(f"[OK] Se guardó una copia en: '{nombre_alternativo}'")
    
    print("\n[INFO] Abriendo ventana interactiva de Matplotlib...")
    print("(Puedes interactuar con los botones de zoom/pan; cierra la ventana para finalizar el script).")
    plt.show()
    plt.close()

def main():
    print("=" * 60)
    print("         EJEMPLO DE LA LIBRERÍA: MATPLOTLIB")
    print("=" * 60)
    generar_graficas()

if __name__ == "__main__":
    main()
