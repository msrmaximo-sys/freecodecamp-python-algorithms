# Estructuras de datos

Entender cómo se pueden organizar elementos y recorrer sus relaciones.

## Ejercicios

| Archivo | Qué practica |
| --- | --- |
| [20ListaEnlazada.py](20ListaEnlazada.py) | Lista enlazada. Nodos con un valor y una referencia al siguiente; inserción, eliminación y longitud. |

## Cómo leer este bloque

A diferencia de una lista de Python, esta implementación conecta objetos Node mediante el atributo `next`. Para agregar al final o buscar un elemento para eliminar, recorre los nodos desde la cabeza. La [tabla hash](../../proyectos-certificacion/tabla-hash/) amplía este tema y se conserva en certificación para evitar duplicar código.

## Ejecución

Desde la raíz del repositorio, en PowerShell:

```powershell
py ejercicios/04-estructuras-de-datos/20ListaEnlazada.py
```

Podés sustituir el nombre por otro archivo de la tabla. Si el archivo solo define funciones o clases, ejecutarlo no muestra necesariamente un resultado. Usá `py -i ruta/al/archivo.py` para cargarlo y luego llamar a sus funciones en la consola de Python. Para salir de esa consola, escribí `exit()`.

## Tecnologías

Python 3 y su biblioteca estándar. No hace falta instalar paquetes con pip. En un equipo sin el comando `py`, se puede usar `python` o `python3` según la instalación.

[Volver al índice del repositorio](../../README.md)
