# Programación orientada a objetos

Representar entidades con clases que reúnen datos y comportamientos.

## Ejercicios

| Archivo | Qué practica |
| --- | --- |
| [10ClasesPrac.py](10ClasesPrac.py) | Primeras clases. Atributos y métodos; inspección y eliminación de atributos en una sesión de ejemplo. |
| [11Orbita.py](11Orbita.py) | Planetas. Validación en el constructor y representación de objetos con __str__. |
| [12Email.py](12Email.py) | Simulador de correo. Colaboración entre Email, User e Inbox para enviar y leer mensajes en memoria. |
| [16.1CatalogoPelis.py](16.1CatalogoPelis.py) | Catálogo básico. Clases Movie, TVSeries y MediaCatalogue para guardar y mostrar contenido. |
| [14CatalogoMultimedia.py](14CatalogoMultimedia.py) | Catálogo con validaciones. Herencia, filtrado por tipo y una excepción propia para elementos no admitidos. |
| [15Personaje.py](15Personaje.py) | Personaje de juego. Propiedades que controlan salud y maná, junto con cambios de nivel. |
| [17MotorDescuento.py](17MotorDescuento.py) | Motor de descuentos. Clases de estrategias con una interfaz común para elegir el mejor precio aplicable. |
| [18InterfazPlayer.py](18InterfazPlayer.py) | Jugador y peón. Clase abstracta, herencia y movimientos aleatorios. |

## Cómo leer este bloque

Una clase define qué datos y operaciones tienen sus objetos. La herencia permite extender una clase existente; una clase abstracta establece operaciones que otras clases deben implementar. Conviene leer primero el catálogo básico y después el catálogo con validaciones. El simulador de correo no envía correos reales: trabaja con objetos en memoria.

## Ejecución

Desde la raíz del repositorio, en PowerShell:

```powershell
py ejercicios/03-programacion-orientada-a-objetos/12Email.py
```

Podés sustituir el nombre por otro archivo de la tabla. Si el archivo solo define funciones o clases, ejecutarlo no muestra necesariamente un resultado. Usá `py -i ruta/al/archivo.py` para cargarlo y luego llamar a sus funciones en la consola de Python. Para salir de esa consola, escribí `exit()`.

## Tecnologías

Python 3 y su biblioteca estándar. No hace falta instalar paquetes con pip. En un equipo sin el comando `py`, se puede usar `python` o `python3` según la instalación.

[Volver al índice del repositorio](../../README.md)
