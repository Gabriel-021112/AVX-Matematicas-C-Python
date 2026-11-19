# simple.py
import ctypes
import os
import platform
import numpy as np

# --- cargar la biblioteca ---
aqui = os.path.dirname(os.path.abspath(__file__))
nombre = "simple.dll" if platform.system() == "Windows" else "libsimple.so"
lib = ctypes.CDLL(os.path.join(aqui, nombre))

# --- declarar tipos de cada función ---
fptr = ctypes.POINTER(ctypes.c_float)
size = ctypes.c_size_t

lib.cuadrado.argtypes = [fptr, fptr, size]
lib.cuadrado.restype = None

lib.raiz.argtypes = [fptr, fptr, size]
lib.raiz.restype = None

lib.limitar.argtypes = [fptr, fptr, size, ctypes.c_float, ctypes.c_float]
lib.limitar.restype = None

lib.producto_punto.argtypes = [fptr, fptr, size]
lib.producto_punto.restype = ctypes.c_float


def _arr(a):
    """Convierte a arreglo float32 contiguo."""
    return np.ascontiguousarray(a, dtype=np.float32)

def _ptr(a):
    return a.ctypes.data_as(fptr)


# --- funciones que se usan desde Python ---
def cuadrado(a):
    a = _arr(a)
    out = np.empty_like(a)
    lib.cuadrado(_ptr(a), _ptr(out), a.size)
    return out

def raiz(a):
    a = _arr(a)
    out = np.empty_like(a)
    lib.raiz(_ptr(a), _ptr(out), a.size)
    return out

def limitar(a, minimo, maximo):
    a = _arr(a)
    out = np.empty_like(a)
    lib.limitar(_ptr(a), _ptr(out), a.size, minimo, maximo)
    return out

def producto_punto(a, b):
    a, b = _arr(a), _arr(b)
    if a.size != b.size:
        raise ValueError("los vectores deben tener el mismo tamaño")
    return lib.producto_punto(_ptr(a), _ptr(b), a.size)
