# Gestor de configuración de usuario

Administrar opciones de un usuario en un diccionario mediante funciones para agregar, actualizar, eliminar y consultar configuraciones.

Solución de práctica de un proyecto de certificación de freeCodeCamp.

[Enunciado oficial](https://www.freecodecamp.org/espanol/learn/python-v9/lab-user-configuration-manager/build-a-user-configuration-manager) · [Ver código](7CERTIFICACION_GestorConfigUsuario.py)

## Qué hace y cómo está organizado

- `add_setting`: agrega una clave si todavía no existe.
- `update_setting`: cambia el valor de una clave existente.
- `delete_setting`: elimina una configuración.
- `view_settings`: devuelve un resumen de las opciones guardadas.

## Conceptos practicados

Diccionarios, tuplas, funciones, condicionales, cadenas y valores de retorno.

## Tecnologías

Python 3 y tipos incorporados; sin bibliotecas externas.

## Cómo ejecutarlo

Desde la raíz del repositorio, en PowerShell:

```powershell
cd proyectos-certificacion/gestor-configuracion-usuario
py -i 7CERTIFICACION_GestorConfigUsuario.py
```

Después, en la consola de Python:

```python
configuracion = {}
print(add_setting(configuracion, ("tema", "oscuro")))
print(update_setting(configuracion, ("tema", "claro")))
print(view_settings(configuracion))
```

Para salir, escribí `exit()`.

En equipos sin `py`, usá `python` o `python3` según la instalación. Para volver a la raíz del repositorio desde esta carpeta, ejecutá `cd ../..` en PowerShell.

## Alcance y observaciones

Las funciones de alta y actualización convierten claves y valores a minúsculas. Los datos viven en memoria: no se guardan en un archivo ni en una base de datos. Las funciones esperan cadenas en las configuraciones.

[Volver al índice del repositorio](../../README.md)
