import random
import numpy as np
contador = 0

matriz = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        matriz[i][j] = random.randint(1, 20)
        if matriz[i][j] > 10:
            contador +=1
print(matriz)
print("Os valores maiores que 10 são: ", contador)