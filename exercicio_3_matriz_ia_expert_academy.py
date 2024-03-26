import numpy as np

Tamanho = 3

matrizA = np.empty((Tamanho, Tamanho), dtype=int)

matrizB = np.empty((Tamanho, Tamanho), dtype=int)

matrizC = np.empty((Tamanho, Tamanho), dtype=int)

for linha in range(Tamanho):
    for coluna in range(Tamanho):
        valor = int(input(f"Digite o valor da linha {linha} e coluna {coluna}: "))

        matrizA[linha][coluna] = valor

print('\n')

for linha in range(Tamanho):
    for coluna in range(Tamanho):
        valor = int(input(f"Digite o valor da linha {linha} e coluna {coluna}: "))

        matrizB[linha][coluna] = valor

print('\n')

matrizC = matrizA + matrizB

print(matrizC)
