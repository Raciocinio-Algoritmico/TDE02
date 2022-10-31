#Declaração do vetor que será preenchido
vetor = []

#Preenche o vetor com valores inseridos pelo usuário
while True:
    valor = int(input("Digite um número: "))
    #Checa se o valor digitado pelo usuário é positivo
    if valor >= 0:
        #Se for, criamos uma novo vetor com um único valor 0 (caixinha)
        #e concatenamos com o vetor original vazio
        vetor = vetor + [0]
        #inserimos na última posição do vetor o valor digitado
        #os valores devem ser inseridos sempre no final para ficar na ordem que foram digitados
        vetor[-1] = valor
    else:
        #caso o valor seja negativo sai do loop
        break

#Imprime o vetor preenchido
print(vetor)

#Variáveis auxiliares para armazenar os valores solicitados pelo exercício
maiores = 0
pares = 0
impares = 0

#Percorre o vetor
for indice in range(len(vetor)):
    #Se o valor atual for maior que 5
    if vetor[indice] > 5:
        #Soma o valor um na variável maiores (Contagem de valores maior que 5)
        maiores += 1

    #Se o valor atual for par
    if vetor[indice] % 2 == 0:
        #Realiza soma acumulada dos valores pares
        pares += vetor[indice]
    #Caso o valor seja ímpar
    else:
        #Realiza soma acumulado dos valores ímpares
        impares += vetor[indice]

#Imprime os valores solicitados no exercício
print(f'A quantidade de valores maiores que 5 é: {maiores}')
print(f'A soma dos pares é: {pares}')
print(f'A soma dos ímpares é: {impares}')
print(f'A quantidade total de valores é: {len(vetor)}')

