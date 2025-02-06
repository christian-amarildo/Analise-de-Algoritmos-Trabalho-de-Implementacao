import time
import random
import matplotlib.pyplot as plt

# Implementação do QuickSort com escolha de pivô

def particionar(arranjo, inicio, fim, comparacoes, trocas, tipo_pivo):
    if tipo_pivo == 1:
        pivo_indice = fim  # Último elemento
    elif tipo_pivo == 2:
        pivo_indice = random.randint(inicio, fim)  # Aleatório
    elif tipo_pivo == 3:
        pivo_indice = (inicio + fim) // 2  # Elemento do meio
    
    arranjo[pivo_indice], arranjo[fim] = arranjo[fim], arranjo[pivo_indice]  # Troca o pivô para o fim
    pivo = arranjo[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        comparacoes[0] += 1
        if arranjo[j] <= pivo:
            i += 1
            arranjo[i], arranjo[j] = arranjo[j], arranjo[i]
            trocas[0] += 1
    arranjo[i + 1], arranjo[fim] = arranjo[fim], arranjo[i + 1]
    trocas[0] += 1
    return i + 1

def quicksort(arranjo, inicio, fim, comparacoes, trocas, tipo_pivo):
    if inicio < fim:
        pi = particionar(arranjo, inicio, fim, comparacoes, trocas, tipo_pivo)
        quicksort(arranjo, inicio, pi - 1, comparacoes, trocas, tipo_pivo)
        quicksort(arranjo, pi + 1, fim, comparacoes, trocas, tipo_pivo)

def ordenar_quicksort(arranjo, tipo_pivo=1):
    comparacoes = [0]
    trocas = [0]
    quicksort(arranjo, 0, len(arranjo) - 1, comparacoes, trocas, tipo_pivo)
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
tamanhos = [i * 100 for i in range(1, 101)]
#tipos = ["ordenado", "ordenado_decrescente", "aleatorio","valores_repetidos", "parcialmente_ordenado"]
tipos = ["aleatorio"]
resultados = {tipo: [] for tipo in tipos}

# Escolher tipo de pivô (1: fim, 2: aleatório, 3: meio)
tipo_pivo = 1  # Pode ser alterado para 1, 2 ou 3

match tipo_pivo:
    case 1:
        nome_pivo = "Elemento Final"
    case 2:
        nome_pivo = "Elemento Aleatorio"
    
    case 3:
        nome_pivo = "Elemento do Meio"

trocas_totais = []
for tamanho in tamanhos:
    for tipo in tipos:
        vetor = gerar_vetor(tipo, tamanho)
        inicio_tempo = time.time()
        _,trocas=ordenar_quicksort(vetor, tipo_pivo)
        trocas_totais.append(trocas)
        fim_tempo = time.time()
        tempo_execucao = fim_tempo - inicio_tempo
        resultados[tipo].append(tempo_execucao)

print("Vetor de trocasarações para cada tamanho de entrada:", trocas_totais)
# Criar gráfico
plt.figure(figsize=(20, 12))
for tipo in tipos:
    plt.plot(tamanhos, resultados[tipo], label=tipo.replace("_", " ").capitalize())

plt.xlabel("Tamanho do vetor")
plt.ylabel("Tempo de execução (s)")
plt.title(f"Desempenho do QuickSort para diferentes tipos de entrada (Pivô {nome_pivo})")
plt.legend()
plt.grid(True)
plt.show()
