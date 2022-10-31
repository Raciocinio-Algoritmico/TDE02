#Declara o vetor com os valores
vetor = [1, 0, 5, -2, -5, 7]

#Soma as posições 0, 1 e 5 do vetor e armazena na variável
somaPosicoes = vetor[0] + vetor[1] + vetor[5]
#Imprime soma
print(f'Soma = {somaPosicoes}')

#Altera o valor na posição 4 para 100
vetor[4] = 100

#Imprime o vetor com cada valor em uma linha
for indice in range(6):
    print(vetor[indice])