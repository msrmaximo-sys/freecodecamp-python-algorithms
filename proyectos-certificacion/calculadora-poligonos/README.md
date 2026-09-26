# Calculadora de polígonos

Modelar rectángulos y cuadrados para calcular sus medidas y representarlos con caracteres.

Solución de práctica de un proyecto de certificación de freeCodeCamp.

[Enunciado oficial](https://www.freecodecamp.org/espanol/learn/python-v9/lab-polygon-area-calculator/build-a-polygon-area-calculator) · [Ver código](19CERTIFICACION_CalculadoraPoligonos.py)

## Qué hace y cómo está organizado

- `Rectangle` permite consultar área, perímetro y diagonal.
- `Square` hereda de Rectangle y mantiene sus lados iguales al modificarlos.
- `get_picture` dibuja la figura con asteriscos cuando las dimensiones no superan 50.
- `get_amount_inside` calcula cuántas figuras caben por filas y columnas, sin rotarlas.

## Conceptos practicados

Herencia, reutilización de métodos, representación con __str__ y operaciones matemáticas.

## Tecnologías

Python 3 y el módulo math de la biblioteca estándar.

## Cómo ejecutarlo

Desde la raíz del repositorio, en PowerShell:

```powershell
cd proyectos-certificacion/calculadora-poligonos
py 19CERTIFICACION_CalculadoraPoligonos.py
```

En equipos sin `py`, usá `python` o `python3` según la instalación. Para volver a la raíz del repositorio desde esta carpeta, ejecutá `cd ../..` en PowerShell.

## Alcance y observaciones

El archivo incluye ejemplos con un rectángulo y un cuadrado. Para dibujar y calcular cuántas figuras caben, se esperan dimensiones enteras positivas. No hay una validación general de dimensiones inválidas.

[Volver al índice del repositorio](../../README.md)
