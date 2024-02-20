pessoas = {}
idade = []

questionario = True
while questionario:
    nome = (input(f"Digite o nome da pessoa: "))
    idade_pessoas = int(input(f"Digite a idade da pessoa: "))

    pessoas[nome] = idade_pessoas
    idade.append(idade_pessoas)

    encerrar = input("Deseja continuar? Sim ou não?: ")
    if encerrar.lower() != 'sim':
        questionario = False

media = sum(idade)/len(idade)
print(f"A média das idades é {media}")

media_final = sum(idade) > media
print(f"O nome das pessoas com idade acima da média são: {nome}")