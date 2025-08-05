# Percolación en Triangulaciones Causales

Este proyecto simula triangulaciones causales sobre árboles de Galton-Watson condicionados a no extinguirse, y aplica modelos de percolación para estimar el valor crítico y características estructurales.

### 📁 Estructura del repositorio

- `src/`: Módulos de simulación:
  - `arbol_gw.py`: Genera árboles con espina (Galton-Watson crítico).
- `notebooks/`: Visualización y experimentación (Jupyter).
- `data/`: Resultados de simulación.
- `figures/`: Gráficos generados.
- `tests/`: (opcional) Pruebas automáticas.

---

## ▶️ Ejecución

```bash
python src/arbol_gw.py
```

Se generará una visualización del árbol, con la espina en rojo.

---

## 📦 Requisitos

```bash
pip install -r requirements.txt
```

---

## 🔍 Objetivos del proyecto

- [x] Simulación de árboles críticos no extintos.
- [ ] Construcción de triangulaciones causales.
- [ ] Aplicación del modelo de percolación.
- [ ] Estimación del valor crítico \( p_c \).
- [ ] Análisis de clústeres (máximo y medio).

---

## 📖 Referencias

Basado en el trabajo de Cerda-Hernández, Yambartsev y Zohren (2017).
