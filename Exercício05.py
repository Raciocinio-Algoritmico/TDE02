##### Solução feita em sala #####

# vetor = [0] * 10
#
# for indice in range(10):
#     adicao = int(input("Digite o valor inteiro: "))
#     vetor[indice] = adicao
#
# semRepeticao = [0] * 10
#
# for i in range(10):
#     menor = min(vetor)
#     vetor.remove(menor)
#     semRepeticao[i] = menor
#
# repete = semRepeticao[0]
# valor = 0
# quantidade = 0
#
# for numRepetido in range(1, 10):
#     if repete == semRepeticao[numRepetido]:
#         valor = repete
#         quantidade += 1
#     elif repete != semRepeticao[numRepetido] and valor != 0:
#         quantidade += 1
#         print(f'{valor} se repete {quantidade} vezes.')
#         valor = 0
#         quantidade = 0
#
#     repete = semRepeticao[numRepetido]


##### Solução da Profe #####
numeros = [0] * 10
iguais = []

for indice in range(10):
    numeros[indice] = int(input('Digite um valor inteiro: '))

for i in range(10):
    for j in range(i + 1, 10):
        # se o atual for igual ao próximo
        if numeros[i] == numeros[j]:
            iguais = iguais + [0]
            iguais[-1] = numeros[j]
            numeros[j] = -1

        j += 1
    i += 1

print(iguais)