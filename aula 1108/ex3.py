def alunos(RA):
    alunos = {87203: "ativo", 87339: "não ativo", 87531: "ativo"}
    return alunos.get(RA, 'Aluno não encontrado')

RA = int(input("Informe o RA do aluno para saber se está ativo: "))
print(alunos(RA))
