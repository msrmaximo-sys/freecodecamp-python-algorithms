# Torres de Hanoi

Resolver el traslado de una torre de discos entre tres varillas y devolver el historial de estados.

Solución de práctica de un proyecto de certificación de freeCodeCamp.

[Enunciado oficial](https://www.freecodecamp.org/espanol/learn/python-v9/lab-tower-of-hanoi/implement-the-tower-of-hanoi-algorithm) · [Ver código](28CERTIFICACION_AlgoritmoHanoi.py)

## Qué hace y cómo está organizado

- `hanoi_solver` prepara las varillas y arma el texto con el historial.
- `movimiento` resuelve el problema de forma recursiva.
- Para mover n discos, primero mueve n-1 a la varilla auxiliar, luego el mayor al destino y finalmente los n-1 restantes.
- Las copias de las listas preservan cada estado aunque las varillas sigan cambiando.

## Conceptos practicados

Recursión, caso base, listas mutables, copias de listas y separación en funciones.

## Tecnologías

Python 3 y tipos incorporados; sin bibliotecas externas.

## Cómo ejecutarlo

Desde la raíz del repositorio, en PowerShell:

```powershell
cd proyectos-certificacion/torres-de-hanoi
py 28CERTIFICACION_AlgoritmoHanoi.py
```

En equipos sin `py`, usá `python` o `python3` según la instalación. Para volver a la raíz del repositorio desde esta carpeta, ejecutá `cd ../..` en PowerShell.

## Alcance y observaciones

La demostración usa cuatro discos y muestra el estado inicial más los estados de cada movimiento. La implementación actual espera un entero positivo: cero o valores negativos no están contemplados. La cantidad de movimientos es 2**n - 1, por lo que conviene probar con pocos discos.

[Volver al índice del repositorio](../../README.md)
