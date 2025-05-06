import random
import time

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

for size in [1000, 10000]:
    arr = [random.randint(0, 10000) for _ in range(size)]
    start = time.perf_counter()
    insertion_sort(arr)
    end = time.perf_counter()
    print(f"Insertion Sort - Tamanho: {size} elementos | Tempo: {end - start:.6f} segundos")
