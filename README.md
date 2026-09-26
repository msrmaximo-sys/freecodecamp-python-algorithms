# Python: ejercicios y proyectos de freeCodeCamp

Este repositorio reúne mis ejercicios y proyectos realizados durante el aprendizaje de Python en freeCodeCamp. Lo organizo como parte de mi portfolio, con interés en el desarrollo backend y el análisis de sistemas.

El objetivo es mostrar cómo practico lógica, validación de datos, modelado con clases, estructuras de datos y resolución de problemas. Son ejercicios de aprendizaje; cada carpeta explica qué hace el código y cómo probarlo.

**Curso de referencia:** [Python de freeCodeCamp](https://www.freecodecamp.org/espanol/learn/python-v9/).

## Proyectos de certificación

Cada proyecto tiene su explicación, instrucciones y enlace al enunciado oficial.

| Proyecto | Conceptos practicados |
| --- | --- |
| [Gestor de configuración de usuario](proyectos-certificacion/gestor-configuracion-usuario/) | Diccionarios, tuplas, funciones, condicionales, cadenas y valores de retorno. |
| [Aplicación de presupuesto](proyectos-certificacion/aplicacion-presupuesto/) | Clases, métodos, listas de diccionarios, reglas sobre saldos y formato de cadenas. |
| [Calculadora de polígonos](proyectos-certificacion/calculadora-poligonos/) | Herencia, reutilización de métodos, representación con __str__ y operaciones matemáticas. |
| [Tabla hash](proyectos-certificacion/tabla-hash/) | Clases, diccionarios anidados, recorrido de cadenas y colisiones de hash. |
| [Torres de Hanoi](proyectos-certificacion/torres-de-hanoi/) | Recursión, caso base, listas mutables, copias de listas y separación en funciones. |

## Bloques de ejercicios

El recorrido sugerido va desde fundamentos hasta grafos y búsqueda. Los números de las carpetas indican ese orden; los prefijos de los archivos conservan mis referencias de trabajo originales y pueden repetirse.

| Bloque | Archivos Python | Objetivo |
| --- | --- | --- |
| [Fundamentos de Python](ejercicios/01-fundamentos/) | 5 | Practicar cómo representar datos, tomar decisiones y dividir un problema en funciones. |
| [Validación de datos y manejo de errores](ejercicios/02-validacion-y-errores/) | 4 | Comprobar entradas y distinguir entre datos válidos, datos incorrectos y errores de ejecución. |
| [Programación orientada a objetos](ejercicios/03-programacion-orientada-a-objetos/) | 8 | Representar entidades con clases que reúnen datos y comportamientos. |
| [Estructuras de datos](ejercicios/04-estructuras-de-datos/) | 1 | Entender cómo se pueden organizar elementos y recorrer sus relaciones. |
| [Recursión y algoritmos](ejercicios/05-recursion-y-algoritmos/) | 7 | Resolver problemas paso a paso y comparar distintas formas de buscar, ordenar y calcular. |
| [Grafos y búsqueda](ejercicios/06-grafos-y-busqueda/) | 4 | Representar conexiones y explorar caminos o combinaciones posibles. |

En total hay **34 archivos Python: 29 ejercicios y 5 proyectos de certificación**.

## Organización

```text
freecodecamp-python-algorithms/
├── README.md
├── .gitignore
├── proyectos-certificacion/
│   ├── gestor-configuracion-usuario/
│   ├── aplicacion-presupuesto/
│   ├── calculadora-poligonos/
│   ├── tabla-hash/
│   └── torres-de-hanoi/
└── ejercicios/
    ├── 01-fundamentos/
    ├── 02-validacion-y-errores/
    ├── 03-programacion-orientada-a-objetos/
    ├── 04-estructuras-de-datos/
    ├── 05-recursion-y-algoritmos/
    └── 06-grafos-y-busqueda/
```

Cada bloque y cada proyecto cuenta con un README propio. Los proyectos se guardan una sola vez, aunque trabajen conceptos de varios bloques.

## Tecnologías y requisitos

- Python 3.9 o posterior, por las anotaciones como `list[DiscountStrategy]` presentes en el código.
- Biblioteca estándar: `abc`, `datetime`, `math`, `pdb`, `random` y `re`, según el ejercicio.
- Git y GitHub para organizar y publicar el trabajo.

No se necesitan paquetes externos ni un archivo de dependencias para ejecutar estos ejercicios.

## Cómo probar el código

Abrí una terminal en la carpeta del repositorio. En Windows podés comprobar Python y ejecutar un ejemplo así:

```powershell
py --version
py ejercicios/01-fundamentos/1SeleccionTransporte.py
```

Algunos archivos incluyen demostraciones y muestran resultados directamente. Otros solo definen funciones o clases: en esos casos, se pueden cargar de forma interactiva:

```powershell
py -i ejercicios/01-fundamentos/2DefDescuento.py
```

Luego, dentro de Python:

```python
apply_discount(100, 20)
# Resultado: 80.0
exit()
```

En sistemas sin el comando `py`, usá `python` o `python3`, según tu instalación. Revisá el README de cada carpeta para conocer las entradas esperadas y las limitaciones de sus ejemplos.

## Relación con mi aprendizaje

La validación de registros ayuda a practicar requisitos sobre datos. Los catálogos y el presupuesto permiten trabajar entidades, relaciones y reglas. Los algoritmos y las estructuras de datos aportan distintas maneras de organizar información y resolver problemas.

Los nombres de funciones y mensajes requeridos por los ejercicios pueden estar en inglés, mientras que esta documentación está en español. Los enunciados y las actividades de referencia pertenecen a freeCodeCamp; este repositorio reúne mis soluciones y prácticas de aprendizaje.
