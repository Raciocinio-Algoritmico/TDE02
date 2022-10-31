vetor1 = [1, 3, 5, 7, 9]
vetor2 = [2, 4, 6, 8, 10]

vetorResultado = [0] * 10


for i in range(10):
    if i % 2 == 0:
        vetorResultado[i] = vetor1[int(i/2)]
    else:
        vetorResultado[i] = vetor2[int(i/2)]

print(vetorResultado)