from random import randrange

#Cria um vetor vazio de tamanho 50
vetor = [0] * 50

#Variáveis utilitárias para armazenar os valores solicitados
soma = 0
quantidadeDeNoves = 0

#Preenche o vetor criado com valores aleatórios entre 0 e 20
for i in range(50):
    vetor[i] = randrange(21)
    #Imprime o vetor com o índice para verificar se está correto
    print(f'{i} = {vetor[i]}')
    #Realiza a soma acumulada dos valores do vetor
    soma += vetor[i]

    #Verifica se o valor inserido é igual a 9
    if vetor[i] == 9:
        #Realiza a soma acumulada para cada 9 encontrado
        quantidadeDeNoves += 1

#Variáveis utilitárias para armazenar os valores solicitados
maior = vetor[0]
menor = vetor[0]

#Percorre o vetor preenchido para encontrar o maior e o menor
for j in range(1, 50):
    #Se o valor atual for maior que o valor armazenado na variável maior
    if vetor[j] > maior:
        #Então maior vai ser igual ao valor atual
        maior = vetor[j]

    #Se o valor atual for menor que o valor armazenado na variável menor
    if vetor[j] < menor:
        #Então menor vai ser igual ao valor atual
        menor = vetor[j]

#Impressão dos valores encontrados para cada ítem solicitado no exercício
print(f'Soma dos valores: {soma}')
print(f'Quantidade de 9: {quantidadeDeNoves}')
print(f'Número maior: {maior}')
print(f'Número menor: {menor}')