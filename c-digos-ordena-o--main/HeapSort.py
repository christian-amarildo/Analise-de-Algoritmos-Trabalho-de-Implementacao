import time
import random
import matplotlib.pyplot as plt

# Função para heapificar um subárvore enraizada no índice i
def heapificar(arranjo, n, i, comparacoes, trocas):
    maior = i  
    esquerda = 2 * i + 1  
    direita = 2 * i + 2  
    
    if esquerda < n:
        comparacoes[0] += 1
        if arranjo[esquerda] > arranjo[maior]:
            maior = esquerda
    
    if direita < n:
        comparacoes[0] += 1
        if arranjo[direita] > arranjo[maior]:
            maior = direita
    
    if maior != i:
        arranjo[i], arranjo[maior] = arranjo[maior], arranjo[i]
        trocas[0] += 1
        heapificar(arranjo, n, maior, comparacoes, trocas)

# Implementação do Heapsort
def heapsort(arranjo):
    n = len(arranjo)
    comparacoes = [0]
    trocas = [0]
    
    for i in range(n // 2 - 1, -1, -1):
        heapificar(arranjo, n, i, comparacoes, trocas)
    
    for i in range(n - 1, 0, -1):
        arranjo[i], arranjo[0] = arranjo[0], arranjo[i]
        trocas[0] += 1
        heapificar(arranjo, i, 0, comparacoes, trocas)
    
    return comparacoes[0], trocas[0]

# Gerar diferentes tipos de vetores de entrada
def gerar_vetor(tipo, tamanho):
    if tipo == "ordenado":
        return list(range(tamanho))
    elif tipo == "ordenado_decrescente":
        return list(range(tamanho, 0, -1))
    elif tipo == "aleatorio":
        return [random.randint(0, 1000) for _ in range(tamanho)]
    elif tipo == "valores_repetidos":
        return [42] * tamanho
    elif tipo == "parcialmente_ordenado":
        vetor = list(range(tamanho))
        random.shuffle(vetor[:tamanho // 2])  # Desordena metade do vetor
        return vetor

# Testar tempos de execução para diferentes tamanhos de entrada
tamanhos = [i*100 for i in range(1,101)]
#tipos = ["ordenado", "ordenado_decrescente", "aleatorio", "valores_repetidos", "parcialmente_ordenado"]
tipos = ["aleatorio"]
resultados = {tipo: [] for tipo in tipos}

trocas_totais = []
for tamanho in tamanhos:
    for tipo in tipos:
        vetor = gerar_vetor(tipo, tamanho)
        inicio_tempo = time.time()
        _, trocas = heapsort(vetor)
        trocas_totais.append(trocas)
        fim_tempo = time.time()
        tempo_execucao = fim_tempo - inicio_tempo
        resultados[tipo].append(tempo_execucao)




print("Vetor de trocas para cada tamanho de entrada:", trocas_totais)

# Criar gráfico
plt.figure(figsize=(20, 12))
for tipo in tipos:
    plt.plot(tamanhos, resultados[tipo], label=tipo.replace("_", " ").capitalize())

plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo de execução (s)")
plt.title("Desempenho do Heapsort para diferentes tipos de entrada")
plt.legend()
plt.grid(True)
plt.show()
