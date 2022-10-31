vetor = [1, 2, 0, 3, 4, 5, 0, 6, 7, 8, 0, 9, 10, 0, 0]

for i in range(15):
    #se encontrou o 0
    if vetor[i] == 0:
        anterior = vetor[:i]
        proximo = vetor[i+1: len(vetor)]
        vetor = anterior + proximo + [0]


print(vetor)