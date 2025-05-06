import random
import time
import statistics

# Algoritmos de ordenação
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

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

def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def quick_sort(arr):
    a = arr.copy()
    if len(a) <= 1:
        return a
    else:
        pivot = a[len(a) // 2]
        left = [x for x in a if x < pivot]
        middle = [x for x in a if x == pivot]
        right = [x for x in a if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

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

    a = arr.copy()
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

# Parâmetros de experimento
algorithms = {
    "BubbleSort": bubble_sort,
    "InsertionSort": insertion_sort,
    "SelectionSort": selection_sort,
    "QuickSort": quick_sort,
    "MergeSort": merge_sort
}

sizes = [1000]  # apenas 1000 para algoritmos O(n^2)
distributions = {
    "Random": lambda n: [random.randint(0, 10000) for _ in range(n)],
    "Sorted": lambda n: list(range(n)),
    "ReverseSorted": lambda n: list(range(n, 0, -1))
}

# Execução dos experimentos
with open("resultados_execucao.csv", "w") as f:
    f.write("Algorithm,Size,Distribution,MeanTime,StdDev\n")
    for size in sizes:
        for dist_name, dist_func in distributions.items():
            for alg_name, alg_func in algorithms.items():
                tempos = []
                for _ in range(30):
                    data = dist_func(size)
                    start = time.perf_counter()
                    alg_func(data)
                    end = time.perf_counter()
                    tempos.append(end - start)
                media = statistics.mean(tempos)
                desvio = statistics.stdev(tempos)
                linha = f"{alg_name},{size},{dist_name},{media:.6f},{desvio:.6f}\n"
                print(linha.strip())
                f.write(linha)
