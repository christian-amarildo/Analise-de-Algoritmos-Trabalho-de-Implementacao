import time
import random
import matplotlib.pyplot as plt

# Implementação dos algoritmos de ordenação

def heapificar(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapificar(arr, n, maior)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapificar(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapificar(arr, i, 0)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[len(arr) // 2]
    esquerda = [x for x in arr if x < pivo]
    meio = [x for x in arr if x == pivo]
    direita = [x for x in arr if x > pivo]
    return quick_sort(esquerda) + meio + quick_sort(direita)

def shell_sort(arr):
    n = len(arr)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = arr[i]
            j = i
            while j >= intervalo and arr[j - intervalo] > temp:
                arr[j] = arr[j - intervalo]
                j -= intervalo
            arr[j] = temp
        intervalo //= 2

def medir_tempo(funcao_ordenacao, arr):
    inicio = time.time()
    if funcao_ordenacao == quick_sort:
        arr[:] = funcao_ordenacao(arr)
    else:
        funcao_ordenacao(arr)
    fim = time.time()
    return fim - inicio

tamanhos = [i*100 for i in range(1,101)]
tempo_heap_sort = []
tempo_quick_sort = []
tempo_shell_sort = []

for tamanho in tamanhos:
    vetor = [random.randint(0, 100000) for _ in range(tamanho)]
    tempo_heap_sort.append(medir_tempo(heap_sort, vetor.copy()))
    tempo_quick_sort.append(medir_tempo(quick_sort, vetor.copy()))
    tempo_shell_sort.append(medir_tempo(shell_sort, vetor.copy()))

# Criando gráfico
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempo_heap_sort, label='HeapSort')
plt.plot(tamanhos, tempo_quick_sort,  label='QuickSort')
plt.plot(tamanhos, tempo_shell_sort,label='ShellSort')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo de Execução (s)')
plt.title('Comparação de Algoritmos de Ordenação')
plt.legend()
plt.grid(True)
plt.show()
