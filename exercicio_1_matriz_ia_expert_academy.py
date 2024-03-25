import numpy as np

matriz = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
        if i == j:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0

print(matriz)
