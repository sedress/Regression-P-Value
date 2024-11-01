# Análisis de Regresión y Valor-P en Python

Este proyecto implementa un modelo de regresión lineal simple utilizando Python, `statsmodels`, `numpy`, y `pandas` para analizar la relación entre el tamaño de una casa (en pies cuadrados) y su precio (en USD).

## Descripción

Generamos un conjunto de datos simulado de tamaño y precio de casas, y aplicamos una regresión lineal para analizar la relación entre estas variables. Este análisis nos permite observar cómo el tamaño de una casa influye en su precio y calcular el valor-P para evaluar la significancia de la relación.

## Estructura del Código

- **Generación de Datos:** Se crean datos simulados para tamaño y precio de casas.
- **Regresión Lineal:** Usamos `statsmodels.OLS` para ajustar un modelo de regresión lineal y calculamos el resumen estadístico, incluyendo el valor-P.
- **Visualización:** Se grafica la relación entre tamaño y precio, junto con la línea de regresión.

## Ejecución

1. Ejecuta el código para ver el resumen estadístico del modelo de regresión.
2. Observa el gráfico que muestra la relación entre tamaño y precio con la línea de regresión.

## Librerías Necesarias

- `numpy`
- `pandas`
- `statsmodels`
- `matplotlib`

## Resultados

El modelo de regresión proporciona un resumen que incluye el valor-P, el cual ayuda a determinar si el tamaño de una casa es un predictor significativo del precio.

