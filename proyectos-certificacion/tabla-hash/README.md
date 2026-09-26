# Tabla hash

Implementar una tabla que relaciona claves con valores y permite agregar, buscar y eliminar entradas.

Solución de práctica de un proyecto de certificación de freeCodeCamp.

[Enunciado oficial](https://www.freecodecamp.org/espanol/learn/python-v9/lab-hash-table/build-a-hash-table) · [Ver código](21CERTIFICACION_Hash.py)

## Qué hace y cómo está organizado

- `hash` obtiene un número sumando los códigos de los caracteres de una clave.
- `add` guarda el par clave-valor dentro del grupo correspondiente.
- `lookup` busca el valor y devuelve None si no encuentra la clave.
- `remove` elimina una clave si existe.

## Conceptos practicados

Clases, diccionarios anidados, recorrido de cadenas y colisiones de hash.

## Tecnologías

Python 3 y la función incorporada ord; sin bibliotecas externas.

## Cómo ejecutarlo

Desde la raíz del repositorio, en PowerShell:

```powershell
cd proyectos-certificacion/tabla-hash
py 21CERTIFICACION_Hash.py
```

En equipos sin `py`, usá `python` o `python3` según la instalación. Para volver a la raíz del repositorio desde esta carpeta, ejecutá `cd ../..` en PowerShell.

## Alcance y observaciones

Dos claves pueden producir el mismo número: eso es una colisión. Esta solución conserva las claves originales en un diccionario dentro de cada grupo. El ejemplo usa fcc y cfc para mostrar ese caso. Es una implementación didáctica sobre diccionarios de Python; la función hash no sirve para proteger contraseñas.

[Volver al índice del repositorio](../../README.md)
