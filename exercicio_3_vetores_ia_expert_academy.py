import numpy as np

vetor_A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
vetor_B = np.array([])

for i in range(len(vetor_A)):
    valor = float(input('Digite um valor: '))
    vetor_A[i] = valor
    vetor_B = valor

vetor_B = vetor_A ** 3

for i in range(len(vetor_A)):
        print(f'O valor de {vetor_A[i]} ao cubo é {vetor_B[i]}')
