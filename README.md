# MLfraude

Proyecto de detección de fraude en transacciones bancarias utilizando técnicas de Machine Learning.

---

## 📁 Estructura del Proyecto

```
MLfraude/
├── src/         # Código fuente (preprocesamiento, entrenamiento, evaluación)
├── notebooks/   # Jupyter Notebooks para EDA, entrenamiento y evaluación
├── data/        # Datos crudos y procesados (no versionados)
├── models/      # Modelos entrenados (no versionados)
├── tests/       # Tests automáticos
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Instalación

1. Clona el repositorio:
  ```bash
  git clone https://github.com/tu_usuario/MLfraude.git
  cd MLfraude
  ```

2. Instala las dependencias:
  ```bash
  pip install -r requirements.txt
  ```

---

## 🚀 Uso

### 1. Preprocesamiento y entrenamiento

- Ejecuta los notebooks en el orden sugerido:
  1. `notebooks/1_EDA.ipynb` — Análisis exploratorio de datos
  2. `notebooks/2_Preprocessing.ipynb` — Preprocesamiento y balanceo
  3. `notebooks/3_Training.ipynb` — Entrenamiento de modelos
  4. `notebooks/4_Evaluation.ipynb` — Evaluación y métricas

### 2. Ejecución de tests

Desde la raíz del proyecto:

```bash
python -m tests.test_scripts
python -m tests.test_model
```

O con pytest (recomendado):

```bash
pytest
```

---

## 🧪 Requisitos

- Python 3.8+
- Las dependencias están listadas en `requirements.txt`:
  - numpy
  - pandas
  - scikit-learn
  - matplotlib
  - seaborn
  - joblib
  - imbalanced-learn
  - pytest

---

## 📦 Datos y Modelos

**Importante:**  
Los archivos en `data/` y `models/` están ignorados en el repositorio por defecto (`.gitignore`).  
Debes colocar el dataset original en `data/raw/creditcard.csv` para ejecutar los notebooks.

---

## 🤝 Contribución

1. Haz un fork del repositorio.
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y agrega tests.
4. Haz un pull request describiendo tus cambios.

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT.

---

## 📬 Contacto

Para dudas o sugerencias, abre un issue o contacta a [https://github.com/edofighter/MLfraude).

---

## 🧐 Descripción del Proyecto

**MLfraude** es un sistema de detección de fraude en transacciones bancarias basado en Machine Learning.  
El objetivo es identificar automáticamente transacciones fraudulentas utilizando un conjunto de datos real de tarjetas de crédito, donde cada registro representa una transacción etiquetada como "fraude" o "no fraude".

El flujo de trabajo incluye:

- **Análisis exploratorio (EDA):**  
  Visualización y análisis de la distribución de clases, outliers, correlaciones y diferencias entre transacciones fraudulentas y legítimas.

- **Preprocesamiento:**  
  Transformación de variables (por ejemplo, logaritmo del monto, extracción de la hora de la transacción), escalado de variables numéricas y división estratificada en conjuntos de entrenamiento y prueba.

- **Balanceo de clases:**  
  Aplicación de técnicas como **SMOTE** (oversampling sintético) y **RandomUnderSampler** para equilibrar la proporción de fraudes y no fraudes en el conjunto de entrenamiento, mejorando la capacidad de los modelos para detectar fraudes.

- **Modelado:**  
  Entrenamiento y comparación de varios algoritmos de clasificación:
  - Regresión logística
  - Random Forest
  - XGBoost
  - LightGBM  
  Se utiliza validación cruzada estratificada para evaluar el rendimiento de cada modelo.

- **Evaluación:**  
  Cálculo y visualización de métricas clave como matriz de confusión, reporte de clasificación y ROC AUC.  
  Se incluyen gráficos de curvas ROC y análisis de importancia de variables para interpretar los resultados.

Estas técnicas permiten abordar el reto de la detección de fraude en un entorno real, donde los datos están altamente desbalanceados y la precisión en la identificación de fraudes es crítica.

---
