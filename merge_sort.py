
import random
import time

def merge_sort(arr):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

for size in [1000, 10000]:
    arr = [random.randint(0, 10000) for _ in range(size)]
    start = time.perf_counter()
    merge_sort(arr)
    end = time.perf_counter()
    print(f"Merge Sort - Tamanho: {size} elementos | Tempo: {end - start:.6f} segundos")
