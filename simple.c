// simple.c
#include <immintrin.h>
#include <stddef.h>
#include <math.h>

/* out[i] = a[i] * a[i] */
void cuadrado(const float* a, float* out, size_t n) {
    size_t i = 0;
    for (; i + 8 <= n; i += 8) {
        __m256 v = _mm256_loadu_ps(a + i);
        _mm256_storeu_ps(out + i, _mm256_mul_ps(v, v));
    }
    for (; i < n; ++i) out[i] = a[i] * a[i];
}

/* out[i] = sqrt(a[i]) */
void raiz(const float* a, float* out, size_t n) {
    size_t i = 0;
    for (; i + 8 <= n; i += 8) {
        __m256 v = _mm256_loadu_ps(a + i);
        _mm256_storeu_ps(out + i, _mm256_sqrt_ps(v));
    }
    for (; i < n; ++i) out[i] = sqrtf(a[i]);
}

/* Limita cada valor al rango [minimo, maximo] */
void limitar(const float* a, float* out, size_t n, float minimo, float maximo) {
    __m256 vmin = _mm256_set1_ps(minimo);
    __m256 vmax = _mm256_set1_ps(maximo);
    size_t i = 0;
    for (; i + 8 <= n; i += 8) {
        __m256 v = _mm256_loadu_ps(a + i);
        v = _mm256_min_ps(_mm256_max_ps(v, vmin), vmax);
        _mm256_storeu_ps(out + i, v);
    }
    for (; i < n; ++i) {
        float x = a[i];
        if (x < minimo) x = minimo;
        if (x > maximo) x = maximo;
        out[i] = x;
    }
}

/* Producto punto: sum(a[i] * b[i]) */
float producto_punto(const float* a, const float* b, size_t n) {
    __m256 acc = _mm256_setzero_ps();
    size_t i = 0;
    for (; i + 8 <= n; i += 8) {
        __m256 va = _mm256_loadu_ps(a + i);
        __m256 vb = _mm256_loadu_ps(b + i);
        acc = _mm256_add_ps(acc, _mm256_mul_ps(va, vb));
    }
    float t[8];
    _mm256_storeu_ps(t, acc);                 /* sumar los 8 lanes a mano */
    float r = t[0] + t[1] + t[2] + t[3] + t[4] + t[5] + t[6] + t[7];
    for (; i < n; ++i) r += a[i] * b[i];
    return r;
}
