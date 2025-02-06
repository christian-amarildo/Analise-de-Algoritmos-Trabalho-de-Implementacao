import matplotlib.pyplot as plt

# Dados fornecidos
heap_sort_swaps = [582, 1359, 2222, 3115, 4028, 5046, 6039, 7021, 8080, 9039, 10141, 11191, 12326, 13366, 14574, 15678, 16805, 17892, 19012, 20131, 21333, 22485, 23663, 24859, 26093, 27251, 28420, 29634, 30824, 32005, 33210, 34500, 35800, 36960, 38195, 39424, 40541, 41833, 43064, 44193, 45545, 46806, 48142, 49408, 50646, 51925, 53202, 54575, 55722, 57074, 58430, 59652, 60967, 62420, 63654, 64803, 66160, 67484, 68869, 70138, 71485, 72778, 74087, 75352, 76734, 78130, 79444, 80550, 82053, 83308, 84575, 85876, 87172, 88322, 89920, 91283, 92590, 93820, 95303, 96764, 97927, 99291, 100588, 101925, 103373, 104676, 106151, 107414, 108850, 110275, 111683, 112931, 114463, 115951, 117178, 118418, 119959, 121352, 122841, 124163]
quick_sort_swaps = [357, 879, 1492, 1756, 2641, 3284, 3694, 4596, 5720, 6386, 7497, 8046, 9740, 9562, 9508, 11677, 12295, 12560, 16517, 15607, 15671, 16574, 16180, 18243, 18472, 18794, 22777, 22270, 21190, 26562, 25184, 27324, 25975, 30036, 31199, 31705, 33901, 36669, 33443, 34518, 35828, 36483, 38905, 36235, 43561, 47927, 44196, 46253, 46327, 51214, 46864, 49042, 48433, 49885, 53979, 55529, 53161, 52821, 56808, 56067, 67731, 61512, 65118, 63159, 66421, 68827, 69625, 69931, 70394, 67767, 73408, 81108, 73980, 81675, 78646, 88657, 85151, 86068, 84997, 85341, 90974, 88983, 92372, 92509, 90618, 99089, 108526, 101857, 114334, 96362, 110411, 104801, 115709, 117203, 111431, 109671, 109910, 117072, 116180, 126844]
shell_sort_swaps = [413, 1047, 1545, 2469, 3087, 4052, 4310, 6420, 7414, 7908, 8348, 9446, 12650, 10762, 11682, 16544, 14383, 18975, 16479, 17296, 21742, 19955, 20246, 23177, 22641, 27388, 26011, 23966, 26993, 26366, 42709, 42913, 33842, 34048, 36582, 48589, 36422, 37231, 36861, 51671, 102131, 48868, 53813, 46230, 46545, 52322, 46469, 62817, 59570, 57828, 51750, 66347, 59781, 58828, 57404, 64229, 67012, 65354, 69122, 70959, 68500, 94069, 82496, 108155, 74578, 74318, 84114, 83552, 76107, 82018, 77205, 120035, 96343, 83045, 87725, 92169, 101273, 90798, 90677, 108116, 94800, 209118, 121401, 107405, 102652, 102445, 104431, 121472, 123476, 119463, 122354, 102781, 124674, 110957, 110139, 143605, 127916, 125489, 122070, 130740]

# Criando gráfico
plt.figure(figsize=(12, 6))
plt.plot(heap_sort_swaps, label="HeapSort")
plt.plot(quick_sort_swaps, label="QuickSort")
plt.plot(shell_sort_swaps, label="ShellSort")

# Personalizações do gráfico
plt.xlabel("Número de Entradas (Amostras)")
plt.ylabel("Número de Trocas")
plt.title("Comparação do Número de Trocas em Algoritmos de Ordenação")
plt.legend()
plt.grid(True)
plt.show()
