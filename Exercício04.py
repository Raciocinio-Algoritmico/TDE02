#Cria um vetor vazio com tamanho 6
vetor = [0] * 6

#Percorre o vetor para preencher com valores fornecidos pelo usuário
for i in range(6):
    vetor[i] = int(input('Digite um valor inteiro: '))

#Impressão do vetor para conferir os valores
print(vetor)

#Cria um novo vetor e utiliza a técnica slicing do python
#O índice -1 corresponde ao último índice da lista
#Ao colocar :: é a mesma coisa que 
vetorInvertido = vetor[::-1]
#Imprime o vetor invertido
print(vetorInvertido)