valores = []

for i in range(6):
    numeros_inteiros = int(input(f"Digite o {i+1}º número: "))
    valores.append((numeros_inteiros))

valores.reverse()

print("Os valores inteiros na ordem inversa são: ", valores)