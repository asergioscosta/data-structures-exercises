lista = []

for i in range(10):
    numeros = int(input("Digite números inteiros: "))
    lista.append(numeros)

solicitacao = int(input("Digite um número para pesquisar: "))
if solicitacao in lista:
    print(f"O número {solicitacao} está na lista")
else:
    print(f" O {solicitacao} não está na lista")