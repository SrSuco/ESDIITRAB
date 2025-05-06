import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

for size in [1000, 10000]:
    arr = [random.randint(0, 10000) for _ in range(size)]
    start = time.perf_counter()
    quick_sort(arr)
    end = time.perf_counter()
    print(f"Quick Sort - Tamanho: {size} elementos | Tempo: {end - start:.6f} segundos")
