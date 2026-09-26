# Grafos y búsqueda

Representar conexiones y explorar caminos o combinaciones posibles.

## Ejercicios

| Archivo | Qué practica |
| --- | --- |
| [28Dijkstra.py](28Dijkstra.py) | Dijkstra. Cálculo de distancias mínimas y caminos sobre una matriz con pesos. |
| [30ConvertirListaAdyacencia_a_Matriz.py](30ConvertirListaAdyacencia_a_Matriz.py) | Lista de adyacencia a matriz. Conversión de vecinos por nodo a una matriz de conexiones. |
| [31ParentesisBalanceadosBFS.py](31ParentesisBalanceadosBFS.py) | Paréntesis balanceados con BFS. Exploración con una cola para generar combinaciones válidas de paréntesis. |
| [32AlgoritmoBusquedaProfundidad.py](32AlgoritmoBusquedaProfundidad.py) | Búsqueda en profundidad. Recorrido de una matriz de adyacencia usando una pila y nodos visitados. |

## Cómo leer este bloque

Un grafo representa nodos y conexiones. Una matriz de adyacencia guarda esas conexiones en filas y columnas. Dijkstra supone pesos no negativos. La conversión a matriz espera nodos numerados de 0 a n-1. La búsqueda en anchura de este bloque explora estados de paréntesis, mientras que la búsqueda en profundidad recorre un grafo explícito.

## Ejecución

Desde la raíz del repositorio, en PowerShell:

```powershell
py ejercicios/06-grafos-y-busqueda/28Dijkstra.py
```

Podés sustituir el nombre por otro archivo de la tabla. Si el archivo solo define funciones o clases, ejecutarlo no muestra necesariamente un resultado. Usá `py -i ruta/al/archivo.py` para cargarlo y luego llamar a sus funciones en la consola de Python. Para salir de esa consola, escribí `exit()`.

## Tecnologías

Python 3 y su biblioteca estándar. No hace falta instalar paquetes con pip. En un equipo sin el comando `py`, se puede usar `python` o `python3` según la instalación.

[Volver al índice del repositorio](../../README.md)
