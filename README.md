# Computational Enrichment of Bioactive Compounds from Sugarcane By-products

Trabajo basado en: Molina-Cortés et al. (2025), *Scientific Reports* 15:19788.
"Study of two sugarcane by-products as source of secondary metabolites and
heat-induced compounds with potential bioactive applications"

## Objetivo

Tratar los compuestos fenólicos (PCs) y compuestos inducidos por calor (HICs)
identificados en el estudio de melazas y vinazas de caña de azúcar como un
"true-positive set". Usar bases de datos públicas de bioactividad química
como fondo de comparación para:

1. Enriquecer las propiedades biológicas conocidas y predichas de estos compuestos.
2. Identificar características estructurales y fisicoquímicas asociadas a bioactividad.
3. Priorizar moléculas con mayor probabilidad de generar respuestas celulares
   (antioxidante, antiinflamatoria, antiproliferativa, u otras).

## Estructura del repositorio

```
sugarcane-bioactive-compounds/
├── data/
│   ├── raw/          # Datos originales del paper (tablas 3 y 4), sin modificar
│   ├── interim/       # Resultados intermedios (con placeholders, sin validar)
│   └── processed/     # Datos finales validados de cada paso
├── notebooks/          # Notebooks Jupyter, uno por paso metodológico
├── src/                 # Funciones Python reutilizables
├── results/
│   ├── figures/         # Gráficos y estructuras renderizadas
│   └── tables/          # Tablas finales exportadas
├── reports/             # Informes narrativos de cada paso + informe final
└── docs/                # Guía metodológica del profesor y referencias
```

## Pasos del proyecto

1. **Curación del true-positive set** → `notebooks/01_curation_true_positive_set.ipynb`
2. **Enriquecimiento de bioactividad** → `notebooks/02_bioactivity_enrichment.ipynb`
3. **Features estructurales/fisicoquímicos** → `notebooks/03_structural_features.ipynb`
4. **Priorización de moléculas** → `notebooks/04_prioritization.ipynb`

## Cómo reproducir

```bash
# Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Instalar dependencias
pip install -r requirements.txt

# Abrir notebooks en VS Code o Jupyter
jupyter notebook
```

## Fuente de datos

- Molina-Cortés, A., Tobar-Tosse, F., Quimbaya, M., Álvarez-Rivera, G., Cifuentes, A.,
  & Jaramillo-Botero, A. (2025). Study of two sugarcane by-products as source of
  secondary metabolites and heat-induced compounds with potential bioactive
  applications. *Scientific Reports*, 15, 19788.
  https://doi.org/10.1038/s41598-025-03262-7

## Autor

[Tu nombre] — [Curso / Materia] — [Fecha]
