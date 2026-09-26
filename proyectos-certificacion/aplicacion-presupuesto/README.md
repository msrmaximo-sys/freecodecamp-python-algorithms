# Aplicación de presupuesto

Registrar ingresos y gastos por categoría, consultar saldos y representar la proporción de gastos con un gráfico de texto.

Solución de práctica de un proyecto de certificación de freeCodeCamp.

[Enunciado oficial](https://www.freecodecamp.org/espanol/learn/python-v9/lab-budget-app/build-a-budget-app) · [Ver código](13CERTIFICACION_AppPresupuesto.py)

## Qué hace y cómo está organizado

- `Category` reúne el nombre de una categoría y su registro de movimientos (`ledger`).
- `deposit` y `withdraw` registran ingresos y retiros; un retiro requiere saldo suficiente.
- `transfer` mueve dinero entre categorías.
- `create_spend_chart` construye un gráfico de gastos por categoría.

## Conceptos practicados

Clases, métodos, listas de diccionarios, reglas sobre saldos y formato de cadenas.

## Tecnologías

Python 3 y tipos incorporados; sin bibliotecas externas.

## Cómo ejecutarlo

Desde la raíz del repositorio, en PowerShell:

```powershell
cd proyectos-certificacion/aplicacion-presupuesto
py 13CERTIFICACION_AppPresupuesto.py
```

En equipos sin `py`, usá `python` o `python3` según la instalación. Para volver a la raíz del repositorio desde esta carpeta, ejecutá `cd ../..` en PowerShell.

## Alcance y observaciones

El archivo incluye una demostración con Food y Clothing. El gráfico actual requiere categorías con algún gasto total mayor que cero; todavía no contempla una lista vacía ni categorías sin gastos. Los movimientos permanecen en memoria. Los importes usan los números de Python tal como se practican en el ejercicio.

[Volver al índice del repositorio](../../README.md)
