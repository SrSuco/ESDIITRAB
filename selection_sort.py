import random
import time

def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

for size in [1000, 10000]:
    arr = [random.randint(0, 10000) for _ in range(size)]
    start = time.perf_counter()
    selection_sort(arr)
    end = time.perf_counter()
    print(f"Selection Sort - Tamanho: {size} elementos | Tempo: {end - start:.6f} segundos")
