
def gravar(rm, nome, serie):
    listaRm.append(rm)
    listaNome.append(nome)
    listaSerie.append(serie)


tuplaRm = ()
listaRm = list(tuplaRm)
tuplaNome = ()
listaNome = list(tuplaNome)
tuplaSerie = ()
listaSerie = list(tuplaSerie)


def cadastro():
    while True:
        zRm = int(input("Informe seu RM: "))
        if zRm in listaRm:
            print("Esse Rm ja existe")
        else:
            if zRm != 0:
                zNome = str(input("Informe seu nome: "))
                zSerie = int(input("Informe sua serie: "))
                if zSerie < 2 or zSerie > 5:
                    print("A serie não existe")
                else:
                    gravar(zRm, zNome, zSerie)
            else:
                return


bloquear = 0


def inscricao():
    alunoRm = int(input("Informe o Rm: "))

    if alunoRm in listaRm:
        posiRm = listaRm.index(alunoRm)
        posiSerie = listaSerie[posiRm]
        # inicio da 2 serie oficina
        if(posiSerie == 2):
            print("As oficinas da sua serie são: ", lisSerOf2)
            of1 = int(input("Escolha uma das opções:"))
            if(of1 == 1):
                if alunoRm in listaOf1:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf1) < 10:
                        listaOf1.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf1), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 2):
                if alunoRm in listaOf2:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf2) < 10:
                        listaOf2.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf2), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 3):
                if alunoRm in listaOf3:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf3) < 10:
                        listaOf3.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf3), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 4):
                if alunoRm in listaOf4:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf4) < 10:
                        listaOf4.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf4), "Inscrições")
                    else:
                        print("Já está lotado")
            # fim da 2 serie oficina
            # inicio da 3 serie oficina
        if(posiSerie == 3):
            print("As oficinas da sua serie são: ", lisSerOf3)
            of1 = int(input("Escolha uma das opções:"))
            if(of1 == 1):
                if alunoRm in listaOf1:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf1) < 10:
                        listaOf1.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf1), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 2):
                if alunoRm in listaOf2:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf2) < 10:
                        listaOf2.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf2), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 3):
                if alunoRm in listaOf5:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf5) < 10:
                        listaOf5.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf5), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 4):
                if alunoRm in listaOf6:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf6) < 10:
                        listaOf6.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf6), "Inscrições")
                    else:
                        print("Já está lotado")
            # fim da 3 serie oficina
         # inicio da 4 serie oficina
        if(posiSerie == 4):
            print("As oficinas da sua serie são: ", lisSerOf4)
            of1 = int(input("Escolha uma das opções:"))
            if(of1 == 1):
                if alunoRm in listaOf7:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf7) < 10:
                        listaOf7.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf7), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 2):
                if alunoRm in listaOf2:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf2) < 10:
                        listaOf2.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf2), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 3):
                if alunoRm in listaOf5:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf5) < 10:
                        listaOf5.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf5), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 4):
                if alunoRm in listaOf8:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf8) < 10:
                        listaOf8.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf8), "Inscrições")
                    else:
                        print("Já está lotado")

            # fim da 4 serie oficina
            # inicio da 5 serie oficina
        if(posiSerie == 5):
            print("As oficinas da sua serie são: ", lisSerOf5)
            of1 = int(input("Escolha uma das opções:"))
            if(of1 == 1):
                if alunoRm in listaOf7:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf7) < 10:
                        listaOf7.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf7), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 2):
                if alunoRm in listaOf2:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf2) < 10:
                        listaOf2.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf2), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 3):
                if alunoRm in listaOf9:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf9) < 10:
                        listaOf9.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf9), "Inscrições")
                    else:
                        print("Já está lotado")
            if(of1 == 4):
                if alunoRm in listaOf10:
                    print("Você ja está inscrito nesta oficina")
                else:
                    if len(listaOf10) < 10:
                        listaOf10.append(alunoRm)
                        print("\nJa foram realizadas: ",
                              len(listaOf10), "Inscrições")
                    else:
                        print("Já está lotado")
            # fim da 5 serie oficina
    else:
        print("Aluno não cadastrado. Favor procurar a coordenação do Fundamental I")
        return


listaOf1 = []
listaOf2 = []
listaOf3 = []
listaOf4 = []
listaOf5 = []
listaOf6 = []
listaOf7 = []
listaOf8 = []
listaOf9 = []
listaOf10 = []
lisSerOf2 = ["1-Criar e contar histórias", " 2-A língua de sinais",
             " 3-O mundo da imaginação", " 4-Criando e recriando com emojis"]
lisSerOf3 = ["1-Criar e contar histórias", " 2-A língua de sinais",
             " 3-Teatro: Luz, Câmera e Ação ", " 4-O corpo fala"]
lisSerOf4 = ["1-Expressão artistica", " 2-A língua de sinais",
             " 3-Teatro: Luz, Câmera e Ação ", " 4-Leitura dramática"]
lisSerOf5 = ["1-Expressão artistica", " 2-A língua de sinais",
             " 3-Soletrando", " 4-Leitura dinâmica"]


def listarInscricao():
    print("\t\tMenu Listar inscrições: ")
    print("1-Listar por aluno ")
    print("2-Listar por oficina ")
    liIns = (int(input("Escolha uma das opções: ")))
    if liIns == 1:
        listaNomeOrd = sorted(listaNome)
        print("******Alunos inscritos - Ordem: Alfabética(nome)******")
        for i in listaNomeOrd:
            if i in listaNome:
                posiLisNome = listaNome.index(i)
                lisRm = listaRm[posiLisNome]
                lisSerie = listaSerie[posiLisNome]
                print("\n", "RM:", lisRm, " - ", i, " - ", lisSerie, "°série")
                print("Oficinas:")
                if lisRm in listaOf1:
                    print("Criar e contar histórias - 2°feira - Matutino")
                if lisRm in listaOf2:
                    print("A lingua de sinais - 4°feira - Matutino")
                if lisRm in listaOf3:
                    print("O mundo da imaginação - 4°feira - Vespertino")
                if lisRm in listaOf4:
                    print("Criando e recriando com emojis - 6°feira - Vespertino")
                if lisRm in listaOf5:
                    print("Teatro: Luz, Câmera e Ação - 3°feira - Matutino")
                if lisRm in listaOf6:
                    print("O corpo fala - 3°feira - Vespertino")
                if lisRm in listaOf7:
                    print("Expressão artistica - 5°feira - Matutino")
                if lisRm in listaOf8:
                    print("Leitura dramática - 2°feira - Vespertino")
                if lisRm in listaOf9:
                    print("Soletrando - 6°feira - Matutino")
                if lisRm in listaOf10:
                    print("Leitura dinâmica - 5°feira - Vespertino")
    elif liIns == 2:        
        print("******Alunos inscritos - Ordem: Alfabética(oficinas)******") 
        print("Oficinas")
        print("A lingua de sinais - 4°feira - Matutino")
        for of2 in listaOf2:
            if of2 in listaRm:
                posiOf2 = listaRm.index(of2)
                contNome = listaNome[posiOf2]
                contSerie = listaSerie[posiOf2] 
                print("RM: ", of2, " - ", contNome, " - ", contSerie, "série")
        print("\nTotal: ", len(listaOf2), "aluno")        
        print("----------------------------------------------") 
        print("Criando e recriando com emojis - 6°feira - Vespertino")       
        for of4 in listaOf4:
            if of4 in listaRm:
                posiOf4 = listaRm.index(of4)
                contNome = listaNome[posiOf4]
                contSerie = listaSerie[posiOf4]
                print("RM: ", of4, " - ", contNome, " - ", contSerie, "série")
        print("\nTotal: ", len(listaOf4), "aluno") 
        print("----------------------------------------------") 
        print("Criar e contar histórias - 2°feira - Matutino")       
        for of1 in listaOf1:
            if of1 in listaRm:
                posiOf1 = listaRm.index(of1)
                contNome = listaNome[posiOf1]
                contSerie = listaSerie[posiOf1]
                print("RM: ", of1, " - ", contNome, " - ", contSerie, "série")
        print("\nTotal: ", len(listaOf1), "aluno") 
        print("----------------------------------------------")
        print("Expressão artistica - 5°feira - Matutino")       
        for of7 in listaOf7:
            if of7 in listaRm:
                posiOf7 = listaRm.index(of7)
                contNome = listaNome[posiOf7]
                contSerie = listaSerie[posiOf7]
                print("RM: ", of7, " - ", contNome, " - ", contSerie, "série")
        print("\nTotal: ", len(listaOf7), "aluno") 
        print("----------------------------------------------")  
        print("Leitura dinâmica - 5°feira - Vespertino")       
        for of10 in listaOf10:
            if of10 in listaRm:
                posiOf10 = listaRm.index(of10)
                contNome = listaNome[posiOf10]
                contSerie = listaSerie[posiOf10]
                print("RM: ", of10, " - ", contNome, " - ", contSerie, "série")
        print("\nTotal: ", len(listaOf10), "aluno") 
        print("----------------------------------------------")
        print("Leitura dramática - 2°feira - Vespertino")       
        for of8 in listaOf8:
            if of8 in listaRm:
                posiOf8 = listaRm.index(of8)
                contNome = listaNome[posiOf8]
                contSerie = listaSerie[posiOf8]
                print("RM: ", of8, " - ", contNome, " - ", contSerie, "série")
        print("\nTotal: ", len(listaOf8), "aluno") 
        print("----------------------------------------------") 
        print("O corpo fala - 3°feira - Vespertino")       
        for of6 in listaOf6:
            if of6 in listaRm:
                posiOf6 = listaRm.index(of6)
                contNome = listaNome[posiOf6]
                contSerie = listaSerie[posiOf6]
                print("RM: ", of6, " - ", contNome, " - ", contSerie, "série")
        print("\nTotal: ", len(listaOf6), "aluno") 
        print("----------------------------------------------")
        print("O mundo da imaginação - 4°feira - Vespertino")       
        for of3 in listaOf3:
            if of3 in listaRm:
                posiOf3 = listaRm.index(of3)
                contNome = listaNome[posiOf3]
                contSerie = listaSerie[posiOf3]
                print("RM: ", of3, " - ", contNome, " - ", contSerie, "série")
        print("\nTotal: ", len(listaOf3), "aluno") 
        print("----------------------------------------------")    
        print("Soletrando - 6°feira - Matutino")       
        for of9 in listaOf9:
            if of9 in listaRm:
                posiOf9 = listaRm.index(of9)
                contNome = listaNome[posiOf9]
                contSerie = listaSerie[posiOf9]
                print("RM: ", of9, " - ", contNome, " - ", contSerie, "série")
        print("\nTotal: ", len(listaOf9), "aluno") 
        print("----------------------------------------------")  
        print("Teatro: Luz, Câmera e Ação - 3°feira - Matutino")       
        for of5 in listaOf5:
            if of5 in listaRm:
                posiOf5 = listaRm.index(of5)
                contNome = listaNome[posiOf5]
                contSerie = listaSerie[posiOf5]
                print("RM: ", of5, " - ", contNome, " - ", contSerie, "série")
        print("\nTotal: ", len(listaOf5), "aluno") 
        print("----------------------------------------------") 

    else:
        return


while True:
    print("Menu de Opções: ")
    print("1 - Cadastrar alunos")
    print("2 - Fazer inscrição")
    print("3 - Listar inscrições")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))
    while opcao < 1 or opcao > 4:
        print("Essa opção não existe")
        opcao = int(input("Informe outra opção: "))

    if opcao == 1 and bloquear == 0:
        cadastro()
        bloquear = bloquear + 1
    elif opcao == 2:
        inscricao()
        if(len(listaOf1) > 9):
            lisSerOf2.pop(0)
            lisSerOf3.pop(0)
        elif(len(listaOf2) > 9):
            lisSerOf2.pop(1)
            lisSerOf3.pop(1)
            lisSerOf4.pop(1)
            lisSerOf5.pop(1)
        elif(len(listaOf3) > 9):
            lisSerOf2.pop(2)
        elif(len(listaOf4) > 9):
            lisSerOf2.pop(3)
        elif(len(listaOf5) > 9):
            lisSerOf3.pop(2)
            lisSerOf4.pop(2)
        elif(len(listaOf6) > 9):
            lisSerOf3.pop(3)
        elif(len(listaOf7) > 9):
            lisSerOf4.pop(0)
            lisSerOf5.pop(0)
        elif(len(listaOf8) > 9):
            lisSerOf4.pop(3)
        elif(len(listaOf9) > 9):
            lisSerOf5.pop(2)
        elif(len(listaOf10) > 9):
            lisSerOf5.pop(3)
    elif opcao == 3:
        listarInscricao()
    else:
        break