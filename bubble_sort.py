import random
import time

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

for size in [1000, 10000]:
    arr = [random.randint(0, 10000) for _ in range(size)]
    start = time.perf_counter()
    bubble_sort(arr)
    end = time.perf_counter()
    print(f"Bubble Sort - Tamanho: {size} elementos | Tempo: {end - start:.6f} segundos")
