
# SIMD-AVX-Python-C

Implementación de operaciones matemáticas vectorizadas utilizando instrucciones SIMD AVX en lenguaje C, con integración a Python mediante ctypes y NumPy.

## Descripción

Este proyecto implementa diferentes operaciones matemáticas aprovechando las instrucciones SIMD AVX de 256 bits. La implementación principal está desarrollada en C, mientras que Python permite utilizar las funciones mediante una biblioteca compartida.

Se utiliza NumPy para manejar los arreglos y comprobar que los resultados obtenidos coincidan con las operaciones equivalentes de esta biblioteca.

## Operaciones implementadas

- **Cuadrado:** calcula el cuadrado de cada elemento de un arreglo.
- **Raíz cuadrada:** calcula la raíz cuadrada de cada elemento.
- **Limitar valores:** restringe los elementos de un arreglo a un intervalo definido.
- **Producto punto:** calcula el producto punto entre dos vectores.

## Tecnologías utilizadas

- Lenguaje C.
- Python 3.
- SIMD AVX (256 bits).
- GCC.
- NumPy.
- ctypes.

## Estructura del proyecto

```text
SIMD-AVX-Python-C/
│
├── prueba.py
├── simple.c
├── simple.py
├── README.md
└── .gitignore
```

## Requisitos

- Linux.
- GCC con soporte para AVX.
- Python 3.
- NumPy.

Instalar NumPy:

```bash
sudo apt install python3-numpy
```

## Compilación

Desde la carpeta del proyecto, ejecutar:

```bash
gcc -O3 -mavx -fPIC -shared simple.c -o libsimple.so -lm
```

Este comando genera la biblioteca compartida `libsimple.so`, que Python utiliza para acceder a las funciones implementadas en C.

## Ejecución

Una vez compilada la biblioteca, ejecutar:

```bash
python3 prueba.py
```

El programa realiza las operaciones matemáticas y compara sus resultados con las funciones equivalentes de NumPy.

## Descripción de los archivos

| Archivo | Descripción |
|---|---|
| `prueba.py` | Ejecuta las pruebas y verifica los resultados. |
| `simple.c` | Contiene las operaciones matemáticas implementadas con AVX. |
| `simple.py` | Conecta Python con la biblioteca C mediante ctypes. |

## Consideraciones

- El procesador debe contar con soporte para instrucciones AVX.
- La compilación utiliza la opción `-mavx`.
- La biblioteca compartida debe estar en el mismo directorio que `simple.py`.
- Los arreglos utilizados en las operaciones se convierten a tipo `float32`.

## Autor

Proyecto académico de programación en C, Python y computación SIMD.
