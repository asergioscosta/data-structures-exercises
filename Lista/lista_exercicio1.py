lista = []

for i in range(10):
    numeros = int(input('Escreva um número inteiro: '))
    lista.append(numeros)

print("Lista:", end=" ")
for numero in lista:
    print(numero, end=" ")