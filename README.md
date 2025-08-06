
# 🌐 Percolación en Triangulaciones Causales

Este proyecto simula y analiza un modelo de **percolación de Bernoulli** sobre **triangulaciones causales críticas** construidas a partir de **árboles de Galton-Watson condicionados a no extinguirse**.

Se sigue la metodología propuesta en el trabajo final del curso de Modelización Matemática y Computacional (UNI), basado en la literatura de Cerda-Hernández et al. (2017).

---

## 📘 Fundamento Teórico

- Una **triangulación causal** representa una descomposición del cilindro \( S \times [0, \infty) \) en triángulos que cumplen ciertas condiciones geométricas y causales.
- Estas triangulaciones se obtienen a partir de árboles aleatorios (Galton-Watson críticos), en donde se condiciona a que no se extingan, formando una espina infinita.
- El modelo de **percolación** se aplica sobre los enlaces de dicha triangulación. Se estudian:
  - El **valor crítico \( p_c \)** para el surgimiento de una componente infinita.
  - El **clúster máximo** y el **clúster medio**.
  - Los exponentes críticos relacionados.

---

## 🧱 Estructura del Proyecto

Cada bloque está documentado en un notebook y se puede ejecutar directamente en Google Colab:

| Bloque | Descripción | Notebook | Enlace Colab |
|--------|-------------|----------|----------------|
| - | Simulación del árbol de Galton-Watson con espina | `simulacion_arbol.ipynb` | https://colab.research.google.com/github/Robertosam/SimulacionAnalisisPercolacionTriangulacionesCausales/blob/main/notebooks/simulacion_arbol.ipynb |
| - | Construcción de la triangulación causal a partir del árbol | `triangulacion_causal.ipynb` | https://colab.research.google.com/github/Robertosam/SimulacionAnalisisPercolacionTriangulacionesCausales/blob/main/notebooks/triangulacion_causal.ipynb |
| - | Modelo de percolación (r-step y s-step) | `percolacion_modelo.ipynb` | https://colab.research.google.com/github/Robertosam/SimulacionAnalisisPercolacionTriangulacionesCausales/blob/main/notebooks/percolacion_modelo.ipynb |
| - | Estimación de $p_c$, clúster máximo y medio | `estimacion_pc_clusters.ipynb` | https://colab.research.google.com/github/Robertosam/SimulacionAnalisisPercolacionTriangulacionesCausales/blob/main/notebooks/estimacion_pc_clusters.ipynb |


---

## ▶️ Requisitos

Instala los paquetes necesarios:

```bash
pip install numpy matplotlib networkx
```

---

## 📌 Créditos

Basado en:
- Cerda-Hernández J, Yambartsev A, Zohren S (2017). *On the critical probability of percolation on random causal triangulations*. Brazilian Journal of Probability and Statistics.

Proyecto desarrollado como parte del curso de modelación de sistemas aleatorios - UNI (Maestría en Modelización Matemática y Computacional).
