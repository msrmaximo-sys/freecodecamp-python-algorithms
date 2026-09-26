# Validación de datos y manejo de errores

Comprobar entradas y distinguir entre datos válidos, datos incorrectos y errores de ejecución.

## Ejercicios

| Archivo | Qué practica |
| --- | --- |
| [6Medico.py](6Medico.py) | Validador de registros médicos. Diccionarios, conjuntos y expresiones regulares para revisar campos de registros de ejemplo. |
| [8Depurar.py](8Depurar.py) | Práctica de depuración. Una función de división con llamadas de ejemplo; importa pdb para practicar depuración. |
| [9DepurarISBM.py](9DepurarISBM.py) | Validador ISBN. Comprobación de dígitos de control ISBN-10 e ISBN-13 y manejo de errores de entrada. |
| [27AlgoritmoLuhn.py](27AlgoritmoLuhn.py) | Algoritmo de Luhn. Comprobación de un dígito de control después de quitar espacios y guiones. |

## Cómo leer este bloque

Validar significa revisar si los datos cumplen condiciones antes de usarlos. Luhn comprueba una regla numérica: no verifica que una tarjeta exista. El archivo ISBN deja `main()` comentado para el entorno del curso; para probarlo localmente se puede usar `py -i 9DepurarISBM.py` y luego escribir `main()`.

## Ejecución

Desde la raíz del repositorio, en PowerShell:

```powershell
py ejercicios/02-validacion-y-errores/6Medico.py
```

Podés sustituir el nombre por otro archivo de la tabla. Si el archivo solo define funciones o clases, ejecutarlo no muestra necesariamente un resultado. Usá `py -i ruta/al/archivo.py` para cargarlo y luego llamar a sus funciones en la consola de Python. Para salir de esa consola, escribí `exit()`.

## Tecnologías

Python 3 y su biblioteca estándar. No hace falta instalar paquetes con pip. En un equipo sin el comando `py`, se puede usar `python` o `python3` según la instalación.

[Volver al índice del repositorio](../../README.md)
