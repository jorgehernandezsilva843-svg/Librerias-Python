# Práctica de Librerías Esenciales en Python
### Materia: Tópicos Avanzados de Programación

---

## 📌 Liga del Repositorio
> **Enlace al repositorio en GitHub:**  
> `https://github.com/TU_USUARIO/TU_REPOSITORIO` *(Reemplazar con el enlace de tu repositorio una vez subido)*

---

## 📖 Descripción General
Este proyecto reúne una colección de ejemplos prácticos, modulares y completamente documentados en Python que abarcan **12 de las librerías más importantes y demandadas** en el desarrollo de software moderno:
- **Librerías estándar** (incluidas en Python): `math`, `random`, `datetime`, `csv`.
- **Generación de documentos PDF**: `fpdf2`, `reportlab`.
- **Computación numérica y análisis de datos**: `numpy`, `pandas`.
- **Visualización gráfica**: `matplotlib`.
- **Comunicaciones y redes HTTP**: `requests`.
- **Desarrollo web y APIs**: `Flask`.
- **Inteligencia Artificial y Machine Learning**: `scikit-learn`.

Cada ejemplo ha sido desarrollado siguiendo buenas prácticas de programación, con tipado claro, comentarios detallados y salidas legibles por terminal o en archivos generados (PDFs, imágenes PNG, CSVs).

---

## 📁 Estructura del Proyecto

```text
Librerias Python/
│
├── 01_math_ejemplo.py           # Operaciones matemáticas, trigonometría y combinatoria
├── 02_random_ejemplo.py         # Números pseudoaleatorios, muestreo y barajado
├── 03_datetime_ejemplo.py       # Manejo de fechas, formateo, parseo y deltas
├── 04_csv_ejemplo.py            # Lectura y escritura con reader/writer y DictReader/DictWriter
├── 05_fpdf_ejemplo.py           # Generación de reportes PDF con encabezados y tablas
├── 06_reportlab_ejemplo.py      # Maquetación PDF avanzada usando Platypus y hojas de estilo
├── 07_numpy_ejemplo.py          # Arrays n-dimensionales, broadcasting y álgebra matricial
├── 08_pandas_ejemplo.py         # Series, DataFrames, agrupaciones (groupby) y agregaciones
├── 09_matplotlib_ejemplo.py     # Subplots: líneas, barras, dispersión e histograma
├── 10_requests_ejemplo.py       # Peticiones HTTP GET y POST, consumo de REST APIs y JSON
├── 11_flask_ejemplo.py          # Microservidor web con rutas dinámicas y endpoints REST
├── 12_scikitlearn_ejemplo.py    # Clasificación (Decision Tree) y Regresión Lineal
│
├── requirements.txt             # Dependencias externas del proyecto
├── .gitignore                   # Archivos temporales ignorados por git
└── README.md                    # Documentación detallada del proyecto
```

---

## 🚀 Requisitos e Instalación

### 1. Requisitos Previos
- Python 3.10 o superior (compatible con Python 3.14).
- Administrador de paquetes `pip`.

### 2. Instalación de Dependencias
Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```
*(En Windows también puedes utilizar `py -m pip install -r requirements.txt`)*

---

## 📚 Explicación Detallada de Cada Librería

### 1. `math` (Librería Estándar)
- **Archivo:** [`01_math_ejemplo.py`](01_math_ejemplo.py)
- **¿Qué es?:** Módulo que proporciona acceso a las funciones matemáticas definidas por el estándar C (trigonometría, logaritmos, constantes fundamentales).
- **Aspectos demostrados:**
  - **Constantes:** $\pi$ (`math.pi`), $e$ (`math.e`), $\tau$ (`math.tau`) e infinito (`math.inf`).
  - **Redondeo y truncamiento:** `ceil()` (techo), `floor()` (piso), `trunc()` y valor absoluto flotante `fabs()`.
  - **Potencias y raíces:** `sqrt()` (raíz cuadrada), `pow()` (potencias) e `hypot()` (cálculo de hipotenusa euclidiana).
  - **Logaritmos:** Logaritmo natural `log()`, en base 10 `log10()`, en base 2 `log2()` y exponencial `exp()`.
  - **Trigonometría:** Conversión de grados a radianes (`radians()`), seno (`sin()`), coseno (`cos()`) y tangente (`tan()`).
  - **Combinatoria:** Factorial (`factorial()`), Máximo Común Divisor (`gcd()`), combinaciones (`comb()`) y permutaciones (`perm()`).
- **Ejecución:**
  ```bash
  py 01_math_ejemplo.py
  ```

---

### 2. `random` (Librería Estándar)
- **Archivo:** [`02_random_ejemplo.py`](02_random_ejemplo.py)
- **¿Qué es?:** Módulo generador de números pseudoaleatorios basado en el algoritmo *Mersenne Twister*.
- **Aspectos demostrados:**
  - **Semilla (`seed`):** Permite fijar un estado inicial para asegurar reproducibilidad en pruebas científicas o simulaciones.
  - **Distribuciones uniformes:** Generación de flotantes en $[0.0, 1.0)$ con `random()` y en rangos arbitrarios con `uniform(a, b)`.
  - **Enteros:** `randint(a, b)` (rango cerrado) y `randrange(start, stop, step)` (con paso).
  - **Selección de colecciones:** `choice()` (selección simple), `choices()` (muestreo con reemplazo) y `sample()` (muestreo sin reemplazo).
  - **Permutación:** Barajado aleatorio en sitio (*in-place*) con `shuffle()`.
  - **Simulación:** Ejemplo de lanzamiento simultáneo de dos dados.
- **Ejecución:**
  ```bash
  py 02_random_ejemplo.py
  ```

---

### 3. `datetime` (Librería Estándar)
- **Archivo:** [`03_datetime_ejemplo.py`](03_datetime_ejemplo.py)
- **¿Qué es?:** Librería especializada en manipulación, cálculo, serialización y validación de fechas, horas y zonas horarias.
- **Aspectos demostrados:**
  - **Tiempo presente:** Obtención de marca de tiempo actual (`datetime.now()`) y fecha del día (`date.today()`).
  - **Instanciación:** Creación de instancias personalizadas de `date`, `time` y `datetime`.
  - **Conversión de objeto a texto (`strftime`):** Formateo con directivas (`%d/%m/%Y`, nombres de días y meses).
  - **Parseo de texto a objeto (`strptime`):** Interpretación de cadenas de texto estructuradas para convertirlas en objetos fecha utilizables.
  - **Aritmética temporal (`timedelta`):** Suma y resta de días, horas y minutos a fechas de referencia.
  - **Cálculo de intervalos:** Diferencia exacta de días y horas restantes para fin de año.
- **Ejecución:**
  ```bash
  py 03_datetime_ejemplo.py
  ```

---

### 4. `csv` (Librería Estándar)
- **Archivo:** [`04_csv_ejemplo.py`](04_csv_ejemplo.py)
- **¿Qué es?:** Módulo para lectura y escritura de archivos en formato CSV (*Comma-Separated Values*), el estándar universal de intercambio de tablas planas.
- **Aspectos demostrados:**
  - **Escritura orientada a diccionarios:** Uso de `csv.DictWriter` con `writeheader()` y `writerows()` para volcar registros estructurados.
  - **Lectura posicional:** Uso de `csv.reader` para procesar filas como listas indexadas numéricamente.
  - **Lectura asociativa:** Uso de `csv.DictReader` para mapear columnas a nombres de llaves, facilitando iteraciones y cálculos agregados (cálculo de promedio general).
  - **Codificación:** Manejo de codificación `utf-8` y parámetro `newline=""` para compatibilidad en sistemas Windows/Linux.
- **Ejecución:**
  ```bash
  py 04_csv_ejemplo.py
  ```
  *(Genera el archivo local `estudiantes.csv`)*

---

### 5. `fpdf2` (Librería Externa)
- **Archivo:** [`05_fpdf_ejemplo.py`](05_fpdf_ejemplo.py)
- **¿Qué es?:** Motor ligero y flexible para la creación programática de documentos PDF en Python, sucesor moderno de `fpdf`.
- **Aspectos demostrados:**
  - **Herencia de clases:** Creación de una clase hija de `FPDF` sobreescribiendo los métodos `header()` y `footer()` para membretes y numeración automática de páginas (`{nb}`).
  - **Configuración visual:** Tipografías (`Helvetica`), tamaños, colores RGB (`set_text_color`, `set_fill_color`, `set_draw_color`).
  - **Texto en bloques:** Uso de `multi_cell()` con justificación de texto automática.
  - **Generación de tablas:** Construcción de celdas con bordes, anchos específicos, alineaciones centradas/izquierdas y filas alternadas con fondo de color tipo cebra.
- **Ejecución:**
  ```bash
  py 05_fpdf_ejemplo.py
  ```
  *(Genera el archivo `reporte_fpdf.pdf`)*

---

### 6. `reportlab` (Librería Externa)
- **Archivo:** [`06_reportlab_ejemplo.py`](06_reportlab_ejemplo.py)
- **¿Qué es?:** La biblioteca empresarial de referencia para maquetación y renderizado de PDFs de alta precisión y complejidad editorial en Python.
- **Aspectos demostrados:**
  - **Arquitectura Platypus:** Separación del flujo de contenido (*Story*) del contenedor del documento (`SimpleDocTemplate`).
  - **Hojas de estilo:** Configuración de estilos tipográficos profesionales con `getSampleStyleSheet()` y `ParagraphStyle` (interlineado `leading`, colores hexadecimales, sangrías).
  - **Elementos estructurados:** Uso de objetos `Paragraph`, `Spacer` y `Table`.
  - **Estilizado de tablas con `TableStyle`:** Definición de cuadrículas (`GRID`), paleta corporativa de colores, alineaciones y coloreado alternado de filas (`ROWBACKGROUNDS`).
- **Ejecución:**
  ```bash
  py 06_reportlab_ejemplo.py
  ```
  *(Genera el archivo `reporte_reportlab.pdf`)*

---

### 7. `NumPy` (Librería Externa)
- **Archivo:** [`07_numpy_ejemplo.py`](07_numpy_ejemplo.py)
- **¿Qué es?:** El paquete fundamental para la computación científica en Python. Proporciona estructuras de arreglos multidimensionales homogéneos de alto rendimiento escritos en C/Fortran.
- **Aspectos demostrados:**
  - **Arreglos n-dimensionales (`ndarray`):** Inspección de `ndim` (dimensiones), `shape` (forma), `dtype` (tipo de dato) y `size`.
  - **Constructores especiales:** `np.zeros()`, `np.arange()` y `np.linspace()`.
  - **Vectorización y Broadcasting:** Operaciones aritméticas término a término sin recurrir a bucles `for`.
  - **Estadística descriptiva:** `mean()`, `median()`, `std()`, `min()` y `max()`.
  - **Filtrado booleano (Masking):** Selección directa de elementos que satisfacen condiciones (`arreglo[arreglo >= 80]`).
  - **Álgebra lineal:** Producto punto y multiplicación matricial con `np.dot` / `@`, y cálculo de la matriz transpuesta (`.T`).
- **Ejecución:**
  ```bash
  py 07_numpy_ejemplo.py
  ```

---

### 8. `Pandas` (Librería Externa)
- **Archivo:** [`08_pandas_ejemplo.py`](08_pandas_ejemplo.py)
- **¿Qué es?:** Librería líder en manipulación, limpieza, transformación y análisis estructurado de datos tabulares.
- **Aspectos demostrados:**
  - **Estructuras primarias:** `Series` (1D etiquetado) y `DataFrame` (2D tabular etiquetado).
  - **Inspección estadística:** Generación de métricas automáticas con `describe()`.
  - **Columnas calculadas:** Vectorización sobre columnas para calcular bonos y sueldos netos.
  - **Filtrado condicional:** Filtrado de registros por condiciones relacionales.
  - **Operaciones de agregación (`groupby`):** Agrupación por departamento calculando conteos, promedios y máximos con sintaxis `agg()`.
  - **Exportación:** Guardado directo de la información procesada a un archivo CSV con `to_csv()`.
- **Ejecución:**
  ```bash
  py 08_pandas_ejemplo.py
  ```
  *(Genera el archivo `reporte_empleados_pandas.csv`)*

---

### 9. `Matplotlib` (Librería Externa)
- **Archivo:** [`09_matplotlib_ejemplo.py`](09_matplotlib_ejemplo.py)
- **¿Qué es?:** La librería gráfica más extendida en el ecosistema científico de Python para crear visualizaciones estáticas, animadas e interactivas.
- **Aspectos demostrados:**
  - **Diseño multipanel (`subplots`):** Organización en una cuadrícula $2 \times 2$ con título global (`suptitle`).
  - **1. Gráfica de Líneas:** Funciones trigonométricas con leyendas, cuadrícula punteada y estilos de trazo continuo y segmentado.
  - **2. Gráfica de Barras:** Comparativa de popularidad de lenguajes, coloreado individual y anotaciones de valor sobre cada barra.
  - **3. Diagrama de Dispersión (*Scatter*):** Relación bivariada entre horas de estudio y calificación obtenida.
  - **4. Histograma:** Distribución de frecuencia con partición en bins y estimación de notas.
  - **Exportación a alta resolución:** Guardado automático a imagen PNG en 300 DPI (`plt.savefig`).
- **Ejecución:**
  ```bash
  py 09_matplotlib_ejemplo.py
  ```
  *(Genera el archivo `graficas_matplotlib.png`)*

---

### 10. `Requests` (Librería Externa)
- **Archivo:** [`10_requests_ejemplo.py`](10_requests_ejemplo.py)
- **¿Qué es?:** La librería estándar de facto para realizar peticiones HTTP elegantes, sencillas y robustas en Python.
- **Aspectos demostrados:**
  - **Peticiones `GET`:** Consumo de recursos REST desde una API pública (JSONPlaceholder), verificación de código de estado (`status_code == 200`) y deserialización automática con `.json()`.
  - **Peticiones `POST`:** Envío de payloads en formato JSON serializado con cabeceras `Content-type` y verificación de creación de recurso (`HTTP 201 Created`).
  - **Parámetros de consulta (`params`):** Paso de diccionarios de argumentos para filtrado en la URL (`?postId=1`).
  - **Tolerancia a fallos:** Manejo de excepciones de red y soporte para entornos corporativos/certificados.
- **Ejecución:**
  ```bash
  py 10_requests_ejemplo.py
  ```

---

### 11. `Flask` (Librería Externa)
- **Archivo:** [`11_flask_ejemplo.py`](11_flask_ejemplo.py)
- **¿Qué es?:** Microframework web ligero y modular para Python que permite crear aplicaciones web completas y servicios API RESTful rápidamente.
- **Aspectos demostrados:**
  - **Enrutamiento y decoradores:** Decorador `@app.route` con especificación explícita de métodos HTTP (`GET`, `POST`).
  - **Renderizado de vistas:** Envío de interfaz HTML con estilos modernos en la ruta raíz `/`.
  - **Rutas dinámicas:** Captura de segmentos en la URL (`/api/saludo/<nombre>`).
  - **API REST con JSON:** Generación de respuestas estructuradas con `jsonify()` y códigos de estado HTTP semánticos (`200 OK`, `201 Created`, `400 Bad Request`).
  - **Recepción de payloads JSON:** Lectura del cuerpo de la petición con `request.get_json()`.
  - **Query parameters:** Lectura de variables con `request.args` en el endpoint `/api/calculadora`.
- **Ejecución:**
  ```bash
  py 11_flask_ejemplo.py
  ```
  *Una vez en ejecución, abre tu navegador web en: `http://127.0.0.1:5000`*

---

### 12. `scikit-learn` (Librería Externa)
- **Archivo:** [`12_scikitlearn_ejemplo.py`](12_scikitlearn_ejemplo.py)
- **¿Qué es?:** La biblioteca líder de Machine Learning clásico en Python, que ofrece herramientas eficientes para minería y análisis predictivo de datos.
- **Aspectos demostrados:**
  - **1. Clasificación con Árboles de Decisión (`DecisionTreeClassifier`):**
    - Carga del conjunto de datos canónico *Iris Dataset* (`load_iris`).
    - Particionado de datos en conjuntos de Entrenamiento (80%) y Prueba (20%) con `train_test_split` y estratificación.
    - Entrenamiento del modelo mediante el método `.fit()`.
    - Evaluación cuantitativa: métrica de Exactitud (`accuracy_score`) y reporte completo (`classification_report` con precisión, recall y F1-score).
    - Inferencia con nuevas observaciones desconocidas (`predict` y `predict_proba`).
  - **2. Regresión Lineal (`LinearRegression`):**
    - Modelado de relación continua (Horas de estudio vs Calificación obtenida).
    - Extracción de la recta aprendida: pendiente (`coef_`) e intercepto (`intercept_`).
    - Medición de la bondad de ajuste mediante el coeficiente de determinación $R^2$ (`r2_score`).
    - Predicción de calificaciones numéricas sobre nuevos valores de entrada.
- **Ejecución:**
  ```bash
  py 12_scikitlearn_ejemplo.py
  ```

---

## 🛠️ Cómo Subir Este Proyecto a GitHub

Si deseas subir este proyecto a tu propio repositorio en GitHub, sigue estos sencillos pasos desde la terminal dentro de esta carpeta:

1. **Inicializar el repositorio git:**
   ```bash
   git init
   ```
2. **Agregar los archivos y realizar el primer commit:**
   ```bash
   git add .
   git commit -m "Entrega: Ejemplos de las 12 librerias de Python - Topicos Avanzados"
   ```
3. **Vincular con tu repositorio remoto de GitHub:**
   ```bash
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   ```
4. **Subir los cambios:**
   ```bash
   git push -u origin main
   ```
5. **Actualizar el enlace:**
   Reemplaza el texto en la sección [📌 Liga del Repositorio](#-liga-del-repositorio) de este `README.md` con la URL final de tu repositorio.

---

## 👨‍💻 Autor
- **Estudiante:** Alumno de Tópicos Avanzados de Programación
- **Fecha:** Octubre 2026
