valores = []

for i in range(10):
    numeros_inteiros = int(input(f"Digite o {i+1}º número: "))
    valores.append(numeros_inteiros)

print("Os valores serão: ", valores)

posicao = max(valores)
maior_valor = valores.index(posicao)

print(f"O maior número será {posicao} e sua posição é {maior_valor}")
