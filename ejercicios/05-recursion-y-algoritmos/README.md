# Recursión y algoritmos

Resolver problemas paso a paso y comparar distintas formas de buscar, ordenar y calcular.

## Ejercicios

| Archivo | Qué practica |
| --- | --- |
| [16.2RangoNumeros.py](16.2RangoNumeros.py) | Rango recursivo. Construcción de una lista desde un inicio hasta un final mediante llamadas recursivas. |
| [22BusquedaBinaria.py](22BusquedaBinaria.py) | Búsqueda binaria. Reducción del intervalo de búsqueda sobre una lista ordenada. |
| [23MergeSort.py](23MergeSort.py) | Merge sort. División de una lista, ordenamiento recursivo y combinación de las partes. |
| [24Biseccion.py](24Biseccion.py) | Raíz por bisección. Aproximación de una raíz cuadrada ajustando un intervalo y una tolerancia. |
| [25AlgoritmoQuicksort.py](25AlgoritmoQuicksort.py) | Quicksort. Separación por un pivote en menores, iguales y mayores. |
| [26SelectionSort.py](26SelectionSort.py) | Selection sort. Selección sucesiva del menor elemento y colocación en su posición. |
| [33FibonacciCalculator.py](33FibonacciCalculator.py) | Fibonacci. Construcción iterativa de una secuencia usando los valores anteriores. |

## Cómo leer este bloque

La recursión ocurre cuando una función vuelve a llamarse con un problema más pequeño y termina en un caso base. La búsqueda binaria necesita una lista ordenada. El rango recursivo supone inicio menor o igual que final; Fibonacci supone un índice entero no negativo. Merge sort y selection sort modifican la lista recibida; quicksort devuelve una nueva lista. [Torres de Hanoi](../../proyectos-certificacion/torres-de-hanoi/) es otro ejemplo de recursión.

## Ejecución

Desde la raíz del repositorio, en PowerShell:

```powershell
py ejercicios/05-recursion-y-algoritmos/23MergeSort.py
```

Podés sustituir el nombre por otro archivo de la tabla. Si el archivo solo define funciones o clases, ejecutarlo no muestra necesariamente un resultado. Usá `py -i ruta/al/archivo.py` para cargarlo y luego llamar a sus funciones en la consola de Python. Para salir de esa consola, escribí `exit()`.

## Tecnologías

Python 3 y su biblioteca estándar. No hace falta instalar paquetes con pip. En un equipo sin el comando `py`, se puede usar `python` o `python3` según la instalación.

[Volver al índice del repositorio](../../README.md)
