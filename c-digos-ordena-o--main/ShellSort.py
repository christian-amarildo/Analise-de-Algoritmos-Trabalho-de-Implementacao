import time
import random
import matplotlib.pyplot as plt

# Implementação do ShellSort com a abordagem original (gap = n//2)
def shellsort(arranjo):
    comparacoes = [0]
    trocas = [0]
    n = len(arranjo)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = arranjo[i]
            j = i
            while j >= intervalo and arranjo[j - intervalo] > temp:
                comparacoes[0] += 1
                arranjo[j] = arranjo[j - intervalo]
                trocas[0] += 1
                j -= intervalo
            arranjo[j] = temp
        intervalo //= 2  # Reduz o intervalo pela metade
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
    elif tipo == "pior_caso":
        # Vetor alternando valores altos e baixos para dificultar a ordenação
        return [i if i % 2 == 0 else tamanho - i for i in range(tamanho)]

# Testar tempos de execução para diferentes tamanhos de entrada
tamanhos = [i * 100 for i in range(1, 101)]
#tipos = ["ordenado", "ordenado_decrescente", "aleatorio", "valores_repetidos", "parcialmente_ordenado", "pior_caso"]
tipos = ["aleatorio"]
resultados = {tipo: [] for tipo in tipos}

trocas_totais = []
for tamanho in tamanhos:
    for tipo in tipos:
        vetor = gerar_vetor(tipo, tamanho)
        inicio_tempo = time.time()
        _,trocas=shellsort(vetor)
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
plt.title("Desempenho do ShellSort com abordagem original para diferentes tipos de entrada")
plt.legend()
plt.grid(True)
plt.show()
