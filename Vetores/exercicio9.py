valores = []

for i in range(6):
    numeros_pares = int(input(f"Digite o {i+1}º número: "))
    if numeros_pares %2 == 0:
        valores.append(numeros_pares)

valores.reverse()

print("Os números pares são: ", valores)
