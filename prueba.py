# prueba.py
import numpy as np
import simple

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float32)
b = np.array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2], dtype=np.float32)
v = np.array([-5, -1, 0, 3, 8, 12, 20, 4, 16, 25], dtype=np.float32)

print("a             =", a)
print("cuadrado(a)   =", simple.cuadrado(a))
print("raiz(a)       =", simple.raiz(a))
print("limitar(v,0,10) =", simple.limitar(v, 0, 10))
print("a . b         =", simple.producto_punto(a, b))   # debe dar 110

print("\n¿Coincide con NumPy?")
print("cuadrado :", np.allclose(simple.cuadrado(a), a * a))
print("raiz     :", np.allclose(simple.raiz(a), np.sqrt(a)))
print("limitar  :", np.allclose(simple.limitar(v, 0, 10), np.clip(v, 0, 10)))
print("punto    :", np.isclose(simple.producto_punto(a, b), np.dot(a, b)))
