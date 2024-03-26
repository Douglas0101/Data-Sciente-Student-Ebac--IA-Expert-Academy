import numpy as np

Tamanho = 3

matriz = np.empty((Tamanho, Tamanho), dtype=object)

for linha in range(Tamanho):
    for coluna in range(Tamanho):
        print('Digite o valor da linha {} e da coluna {}: '.format(linha, coluna), end='')
        matriz[linha][coluna] = int(input())

num_pesquisa = int(input('Digite o valor que deseja pesquisar: '))

quantidade = 0
for linha in range(Tamanho):
    for coluna in range(Tamanho):
        if matriz[linha][coluna] == num_pesquisa:
            quantidade += 1

print('O valor {} aparece {} vez(es) na matriz'.format(num_pesquisa, quantidade))
