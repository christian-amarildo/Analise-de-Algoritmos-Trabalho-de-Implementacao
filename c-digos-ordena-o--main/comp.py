import time
import numpy as np
import matplotlib.pyplot as plt

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)
    
    for num in arr:
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1
    right = 2 * i + 2 
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
    
    return arr

def measure_time(sort_function, arr):
    start = time.time()
    sort_function(arr.copy())
    return time.time() - start

sizes = [i*100 for i in range(1,101)]
time_counting = []
time_heap = []

for size in sizes:
    arr = np.random.randint(0, 10000, size)
    time_counting.append(measure_time(counting_sort, arr))
    time_heap.append(measure_time(heap_sort, arr))

plt.figure(figsize=(20, 10))
plt.plot(sizes, time_counting, label='Counting Sort', marker='o')
plt.plot(sizes, time_heap, label='Heap Sort', marker='s')
plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo de execução (s)')
plt.title('Comparação de Tempo: Counting Sort vs Heap Sort')
plt.legend()
plt.grid()
plt.show()
