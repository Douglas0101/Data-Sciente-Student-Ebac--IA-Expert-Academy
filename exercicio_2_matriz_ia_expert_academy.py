import numpy as np

Tamanho = 4

matriz = np.zeros((Tamanho, Tamanho), dtype=int)

for linha in range(Tamanho):
    for coluna in range(Tamanho):
        print('Digite o valor da linha', linha, 'coluna', coluna, ': ')
        matriz[linha][coluna] = int(input())

soma_segunda_linha = 0
soma_segunda_coluna = 0
soma_matriz = 0

for linha in range(Tamanho):
    for coluna in range(Tamanho):
        if coluna == 1:
            soma_segunda_linha = soma_segunda_linha + matriz[linha][coluna]

        if linha == 1:
            soma_segunda_coluna = soma_segunda_coluna + matriz[linha][coluna]

        soma_matriz = soma_matriz + matriz[linha][coluna]

print(f'Soma da segunda linha: {soma_segunda_linha}')
print(f'Soma da segunda coluna: {soma_segunda_coluna}')
print(f'Soma da matriz: {soma_matriz}')
