import numpy as np

matriz = np.zeros((5,5))
for i in range(5):
    matriz[i][i] = 1

print(matriz)