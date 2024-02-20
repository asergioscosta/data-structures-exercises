alunos = {}

quantidade_avaliacoes = int(input("Digite o número de avaliações por aluno: "))
quantidade_alunos = int(input("Digite a quantidade de alunos: "))

for i in range(quantidade_alunos):
    nome_aluno = input(f"Digite o nome do aluno {i+1}: ")
    notas_aluno = []

    for j in range(quantidade_avaliacoes):
        nota = float(input(f"Digite a nota {j+1} do aluno {nome_aluno}: "))
        notas_aluno.append(nota)

    alunos[nome_aluno] = notas_aluno

for nome, notas in alunos.items():
    media = sum(notas) / quantidade_avaliacoes
    print(f"Nome: {nome}, Média: {media:.2f}")

media_turma = sum(sum(notas) for notas in alunos.values()) / (quantidade_avaliacoes * quantidade_alunos)
print("\nMédia da turma:", media_turma)
