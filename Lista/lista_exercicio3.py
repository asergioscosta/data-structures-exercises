lista = []

for i in range(5):
    numeros = float(input("Digite os números: "))
    lista.append(numeros)

soma = sum(lista)
media = soma / len(lista)

quantidade_positivos = 0
quantidade_negativos = 0

for numero in lista:
    if numero >= 0:
        quantidade_positivos += 1
else:
        quantidade_negativos += 1

maior = max(lista)
menor = min(lista)

print(f"A média dos números será: ", media)
print(f"O maior número será: ", maior)
print(f"O menor número será: ", menor)
print(f"A quantidade de números positivos será: ", quantidade_positivos)
print(f"A quantidade de números negativos será: ", quantidade_negativos)