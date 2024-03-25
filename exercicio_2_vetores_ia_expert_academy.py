import numpy as np

vetor_A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in range(len(vetor_A)):
    valor = int(input("Digite um valor: "))
    vetor_A + 1
    vetor_A[i] = valor

pesquisa = int(input("Qual valor deseja pesquisar? "))

if pesquisa in vetor_A:
    print("Achei o valor!")
else:
    print("Valor não foi encontrado!")
