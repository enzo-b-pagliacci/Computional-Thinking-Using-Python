


nome = []
nota = []
i = 0
for n in range(1, 51):
    if n % 2 != 0:
        name = input("Insira o nome do aluno: ")
        nome.append(name)
        grade = float(input("Insira sua nota: "))
        nota.append(grade)
        i+=1
        print(nome[n])


        