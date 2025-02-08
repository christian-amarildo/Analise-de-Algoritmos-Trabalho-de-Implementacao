medalhistas = []
podio = []

while True:
    try:
        input()  # ignora o nome da modalidade
        
        for _ in range(3):
            pais = input().strip()
            podio.append(pais)
        
        for i in range(3):  # percorre o pódio
            encontrado = False
            for j in range(len(medalhistas)): # verifica se o país já está nos medalhistas
                if medalhistas[j][0] == podio[i]:
                    medalhistas[j][i + 1] += 1  # incrementa a medalha correspondente
                    encontrado = True
                    break
            
            if not encontrado:  # se o país não está nos medalhistas
                nova_entrada = [podio[i], 0, 0, 0] # cria uma nova entrada com o país a ser adicionado
                nova_entrada[i + 1] = 1 # incrementa a nova medalha correspondente
                medalhistas.append(nova_entrada) # adiciona o país e suas medalhas
        
        podio.clear()  # Limpa o pódio para a próxima modalidade
    except EOFError:
        break

for i in range(len(medalhistas) - 1, -1, -1): # ordenação decrescente
    for j in range(len(medalhistas) - 1): # trocar caso alguem com mais ouro estiver na frente
        if medalhistas[j][1] < medalhistas[j+1][1]:  
            medalhistas[j+1], medalhistas[j] = medalhistas[j], medalhistas[j+1]
        elif medalhistas[j][1] == medalhistas[j+1][1]: # se os ouros forem iguais
            if medalhistas[j][2] < medalhistas[j+1][2]: # trocar caso alguem com mais prata estiver na frente
                medalhistas[j+1], medalhistas[j] = medalhistas[j], medalhistas[j+1]
            elif medalhistas[j][2] == medalhistas[j+1][2]: # se as pratas forem iguais
                if medalhistas[j][3] < medalhistas[j+1][3]: # trocar caso alguem com mais bronze estiver na frente
                    medalhistas[j+1], medalhistas[j] = medalhistas[j], medalhistas[j+1]
                elif medalhistas[j][3] == medalhistas[j+1][3]: # se os bronzes forem iguais
                    if medalhistas[j][0] > medalhistas[j+1][0]: # ordena em ordem alfabética crescente
                        medalhistas[j+1], medalhistas[j] = medalhistas[j], medalhistas[j+1]

print("Quadro de Medalhas")
for pais in medalhistas: # imprimindo o quadro de medalhas
    print(*pais)
