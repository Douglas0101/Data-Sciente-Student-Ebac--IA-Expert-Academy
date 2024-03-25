import numpy as np

vetor = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

negativos = 0

for i in range(len(vetor)):
    valor = float(input('Insira um valor: '))
    vetor[i] = valor
    negativos = np.count_nonzero(vetor < 0)

print(f'A soma dos elementos do vetor e: {np.sum(vetor)}')
print(f'A média dos elementos do vetor e: {np.mean(vetor)}')

print(f'A quantidade de números negativos no vetor é = {negativos}')
