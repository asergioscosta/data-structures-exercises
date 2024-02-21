#4. Leia uma matriz 4 x 4, imprima a matriz e retorne a localizacao
# (linha e a coluna) do ˜maior valor.
import random
import numpy as np

maior_valor = None
linha = 0
coluna = 0

matriz = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        matriz[i][j] = random.randint(1,30)

print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if maior_valor is None or matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha = i
            coluna = j

print("Linha do maior valor:", linha + 1)
print("Coluna do maior valor:", coluna + 1)