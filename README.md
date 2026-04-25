# PCA + K-Means Clustering — Global Air Quality

Análisis de calidad del aire global mediante reducción de dimensionalidad (PCA) y segmentación no supervisada (K-Means).

**Dataset:** [Global Air Quality and Respiratory Health Outcomes](https://www.kaggle.com/datasets/tfisthis/global-air-quality-and-respiratory-health-outcomes) — 35 000 registros, 15 variables, 10 años (2014–2023).

---

## Estructura del proyecto

```
ciencia_datos_airquality/
├── pca_clustering_airquality.ipynb   # Notebook principal (pipeline completo)
├── global_air_quality.csv            # Dataset fuente
├── data.py                           # Descarga el dataset desde Kaggle vía kagglehub
└── images/                           # Gráficas exportadas (generado al ejecutar el notebook)
```

---

## Pipeline del notebook

El notebook sigue este orden de ejecución y cada sección depende de la anterior:

| Sección | Descripción |
|---------|-------------|
| 1 | Importaciones y configuración global (`SEED = 333`, carpeta `images/`) |
| 2 | Carga del CSV, tipos de datos, valores nulos |
| 2b | **EDA completo:** conversión de tipos, imputación de nulos (mediana/moda), eliminación de duplicados, estadísticas descriptivas, histogramas, boxplots, skewness, outliers por IQR 3× |
| 3 | Selección de las 12 variables numéricas para PCA |
| 4 | Matriz de correlación (condición previa para PCA) |
| 5 | Estandarización con `StandardScaler` |
| 6 | PCA completo → Scree Plot + varianza acumulada |
| 7 | PCA final con `n_80` componentes (≥80 % varianza) → loadings |
| 8 | K-Means: Elbow + Silhouette Score para k en [2, 10] |
| 9 | K-Means final con `k_opt` |
| 10–13 | Visualización de clusters: scatter PCA, silhouette, perfiles, boxplots, evolución temporal |
| 14 | Resumen ejecutivo |

### Variables clave

- **`SEED = 333`** — fijo en todas las llamadas aleatorias.
- **`IMG_DIR = 'images'`** — todas las figuras se guardan aquí con `plt.savefig()` antes de `plt.show()`.
- **`FEATURES`** — lista de 12 columnas numéricas definida en sección 3; usada a lo largo de todo el notebook.
- **`N_COMPONENTS`** — calculado dinámicamente como el mínimo de componentes que explican ≥80 % de varianza.
- **`K_FINAL`** — `k_opt`, el k con mayor Silhouette Score en el rango evaluado.

### Limpieza de datos (sección 2b)

El CSV tiene columnas numéricas en formato `object` (valores con comas, espacios, etc.). La celda de conversión las normaliza con `pd.to_numeric(errors='coerce')`, imputa nulos con mediana, elimina duplicados y remueve outliers con criterio 3×IQR. El dataset pasa de ~36 437 a ~33 657 filas limpias.

---

## Requisitos

```
numpy pandas matplotlib seaborn scikit-learn kagglehub
```

Instalar:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn kagglehub
```

## Descargar el dataset

```bash
python data.py
```

Copia el CSV resultante a la raíz del proyecto como `global_air_quality.csv`.

## Ejecutar el notebook

```bash
jupyter notebook pca_clustering_airquality.ipynb
```

Ejecutar todas las celdas en orden (`Kernel > Restart & Run All`). Al finalizar, la carpeta `images/` contendrá todas las gráficas exportadas.
