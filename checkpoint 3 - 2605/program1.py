def gravar_alunos(rm, nome, serie):
    lRm.append(rm)
    lNome.append(nome)
    lSerie.append(serie)

lRm = []
lNome = []
lSerie = []

def cadastro_usuario():
    while True:
        inptRm = int(input("Digite o RM do aluno: "))
        if inptRm in lRm:
            print("RM já existe!")
        else:
            if inptRm != 0:
                inptNome = input("Digite o nome do aluno: ")
                inptSerie = int(input("Digite a série do aluno: "))
                while inptSerie < 2 or inptSerie > 5:
                    print("Séries de 2 à 5 permitidas")
                    inptSerie = int(input("Digite a série do aluno: "))
                gravar_alunos(inptRm, inptNome, inptSerie)
            else:
                return

bloqueio1 = 0



lOficinas = ['Criar e contar histórias', 'Teatro: Luz, Câmera e Ação', 'A língua de sinais', 'Expressão Artística', 'Soletrando', 'Leitura dramática', 'O corpo fala', 'O mundo da imaginação', 'Leitura dinâmica', 'Criando e recriando emojis' ]

def fazer_inscricoes():
    lOficinasRelacionadas = []

    of0 = 0
    of1 = 0
    of2 = 0
    of3 = 0
    of4 = 0
    of5 = 0
    of6 = 0
    of7 = 0
    of8 = 0
    of9 = 0

    verificaRm = int(input("Insira seu RM: "))
    if verificaRm in lRm:
        rmIdentificado = lRm.index(verificaRm) 
        serieIdentificada = lSerie[rmIdentificado]
        nomeIdentificado = lNome[rmIdentificado]
        if serieIdentificada == 2:
            if of0 < 11:
                lOficinasRelacionadas.append(lOficinas[0])
                if of2 < 11:
                    lOficinasRelacionadas.append(lOficinas[2])
                    if of7 < 11:
                        lOficinasRelacionadas.append(lOficinas[7])
                        if of9 < 11:
                            lOficinasRelacionadas.append(lOficinas[9])
                elif of7 < 11:
                    lOficinasRelacionadas.append(lOficinas[7])
                    if of9 < 11:
                        lOficinasRelacionadas.append(lOficinas[9])
                elif of9 < 11:
                    lOficinasRelacionadas.append(lOficinas[9])
            elif of2 < 11:
                lOficinasRelacionadas.append(lOficinas[2])
                if of7 < 11:
                    lOficinasRelacionadas.append(lOficinas[7])
                    if of9 < 11:
                        lOficinasRelacionadas.append(lOficinas[9])
                elif of9 < 11:
                    lOficinasRelacionadas.append(lOficinas[9])
            elif of7 < 11:
                lOficinasRelacionadas.append(lOficinas[7])
                if of9 < 11:
                    lOficinasRelacionadas.append(lOficinas[9])
            elif of9 < 11:
                lOficinasRelacionadas.append(lOficinas[9])
            else:
                print("Todas as oficinas estão esgotadas.")

        elif serieIdentificada == 3:
            if of0 < 11:
                lOficinasRelacionadas.append(lOficinas[0])
                if of1 < 11:
                    lOficinasRelacionadas.append(lOficinas[1])
                    if of2 < 11:
                        lOficinasRelacionadas.append(lOficinas[2])
                        if of6 < 11:
                            lOficinasRelacionadas.append(lOficinas[6])
                elif of2 < 11:
                    lOficinasRelacionadas.append(lOficinas[2])
                    if of6 < 11:
                        lOficinasRelacionadas.append(lOficinas[6])
                elif of6 < 11:
                    lOficinasRelacionadas.append(lOficinas[6])
            elif of1 < 11:
                lOficinasRelacionadas.append(lOficinas[1])
                if of2 < 11:
                    lOficinasRelacionadas.append(lOficinas[2])
                    if of6 < 11:
                        lOficinasRelacionadas.append(lOficinas[6])
                elif of6 < 11:
                    lOficinasRelacionadas.append(lOficinas[6])
            elif of2 < 11:
                lOficinasRelacionadas.append(lOficinas[2])
                if of6 < 11:
                    lOficinasRelacionadas.append(lOficinas[6])
            elif of6 < 11:
                lOficinasRelacionadas.append(lOficinas[6])
            else:
                print("Todas as oficinas estão esgotadas.")

        elif serieIdentificada == 4:
            if of1 < 11:
                lOficinasRelacionadas.append(lOficinas[1])
                if of2 < 11:
                    lOficinasRelacionadas.append(lOficinas[2])
                    if of3 < 11:
                        lOficinasRelacionadas.append(lOficinas[3])
                        if of5 < 11:
                            lOficinasRelacionadas.append(lOficinas[5])
                elif of3 < 11:
                    lOficinasRelacionadas.append(lOficinas[3])
                    if of5 < 11:
                        lOficinasRelacionadas.append(lOficinas[5])
                elif of5 < 11:
                    lOficinasRelacionadas.append(lOficinas[5])
            elif of2 < 11:
                lOficinasRelacionadas.append(lOficinas[2])
                if of3 < 11:
                    lOficinasRelacionadas.append(lOficinas[3])
                    if of5 < 11:
                        lOficinasRelacionadas.append(lOficinas[5])
                elif of5 < 11:
                    lOficinasRelacionadas.append(lOficinas[5])
            elif of3 < 11:
                lOficinasRelacionadas.append(lOficinas[3])
                if of5 < 11:
                    lOficinasRelacionadas.append(lOficinas[5])
            elif of5 < 11:
                lOficinasRelacionadas.append(lOficinas[5])
            else:
                print("Todas as oficinas estão esgotadas.")


        elif serieIdentificada == 5:
            if of2 < 11:
                lOficinasRelacionadas.append(lOficinas[2])
                if of3 < 11:
                    lOficinasRelacionadas.append(lOficinas[3])
                    if of4 < 11:
                        lOficinasRelacionadas.append(lOficinas[4])
                        if of8 < 11:
                            lOficinasRelacionadas.append(lOficinas[8])
                elif of4 < 11:
                    lOficinasRelacionadas.append(lOficinas[4])
                    if of8 < 11:
                        lOficinasRelacionadas.append(lOficinas[8])
                elif of8 < 11:
                    lOficinasRelacionadas.append(lOficinas[8])
            elif of3 < 11:
                lOficinasRelacionadas.append(lOficinas[3])
                if of4 < 11:
                    lOficinasRelacionadas.append(lOficinas[4])
                    if of8 < 11:
                        lOficinasRelacionadas.append(lOficinas[8])
                elif of8 < 11:
                    lOficinasRelacionadas.append(lOficinas[8])
            elif of4 < 11:
                lOficinasRelacionadas.append(lOficinas[4])
                if of8 < 11:
                    lOficinasRelacionadas.append(lOficinas[8])
            elif of8 < 11:
                lOficinasRelacionadas.append(lOficinas[8])
            else:
                print("Todas as oficinas estão esgotadas.")                
      
        lNomeInscrito = []
        lOficinaInscrita = []
        lSerieInscrita = []
        lRmInscrito = []

        print("As oficinas disponíveis para sua série são: ", lOficinasRelacionadas)
        oficinaEscolhida = input("Digite o nome da oficina: ").lower()
        if oficinaEscolhida == "criar e contar histórias" and nomeIdentificado not in lNomeInscrito:
            of0+= 1
            lOficinasRelacionadas = []
            lNomeInscrito.append[nomeIdentificado]
            lOficinaInscrita.append[oficinaEscolhida]
            lSerieInscrita.append[serieIdentificada]
            lRmInscrito.append[rmIdentificado]
            print("Já foram feitas ", of0, " inscrições.")
            

        elif oficinaEscolhida == "teatro: luz, câmera e ação" and nomeIdentificado not in lNomeInscrito:
            of1+=1
            lOficinasRelacionadas = []
            lNomeInscrito.append[nomeIdentificado]
            lOficinaInscrita.append[oficinaEscolhida]
            lSerieInscrita.append[serieIdentificada]
            lRmInscrito.append[rmIdentificado]
            print("Já foram feitas ", of1, " inscrições.")

        elif oficinaEscolhida == "a língua de sinais" and nomeIdentificado not in lNomeInscrito:
            of2+=1
            lOficinasRelacionadas = []
            lNomeInscrito.append[nomeIdentificado]
            lOficinaInscrita.append[oficinaEscolhida]
            lSerieInscrita.append[serieIdentificada]
            lRmInscrito.append[rmIdentificado]
            print("Já foram feitas ", of2, " inscrições.")

        elif oficinaEscolhida == "expressão artística" and nomeIdentificado not in lNomeInscrito: 
            of3+=1
            lOficinasRelacionadas = []
            lNomeInscrito.append[nomeIdentificado]
            lOficinaInscrita.append[oficinaEscolhida]
            lSerieInscrita.append[serieIdentificada]
            lRmInscrito.append[rmIdentificado]
            print("Já foram feitas ", of3, " inscrições.")

        elif oficinaEscolhida == "soletrando" and nomeIdentificado not in lNomeInscrito:
            of4+=1
            lOficinasRelacionadas = []
            lNomeInscrito.append[nomeIdentificado]
            lOficinaInscrita.append[oficinaEscolhida]
            lSerieInscrita.append[serieIdentificada]
            lRmInscrito.append[rmIdentificado]
            print("Já foram feitas ", of4, " inscrições.")

        elif oficinaEscolhida == "leitura dramática" and nomeIdentificado not in lNomeInscrito:
            of5+=1
            lOficinasRelacionadas = []
            lNomeInscrito.append[nomeIdentificado]
            lOficinaInscrita.append[oficinaEscolhida]
            lSerieInscrita.append[serieIdentificada]
            lRmInscrito.append[rmIdentificado]
            print("Já foram feitas ", of5, " inscrições.")

        elif oficinaEscolhida == "o corpo fala" and nomeIdentificado not in lNomeInscrito:
            of6+=1
            lOficinasRelacionadas = []
            lNomeInscrito.append[nomeIdentificado]
            lOficinaInscrita.append[oficinaEscolhida]
            lSerieInscrita.append[serieIdentificada]
            lRmInscrito.append[rmIdentificado]
            print("Já foram feitas ", of6, " inscrições.")

        elif oficinaEscolhida == "o mundo da imaginação" and nomeIdentificado not in lNomeInscrito:
            of7+=1
            lOficinasRelacionadas = []
            lNomeInscrito.append[nomeIdentificado]
            lOficinaInscrita.append[oficinaEscolhida]
            lSerieInscrita.append[serieIdentificada]
            lRmInscrito.append[rmIdentificado]
            print("Já foram feitas ", of7, " inscrições.")

        elif oficinaEscolhida == "leitura dinâmica" and nomeIdentificado not in lNomeInscrito: 
            of8+=1
            lOficinasRelacionadas = []
            lNomeInscrito.append[nomeIdentificado]
            lOficinaInscrita.append[oficinaEscolhida]
            lSerieInscrita.append[serieIdentificada]
            lRmInscrito.append[rmIdentificado]
            print("Já foram feitas ", of8, " inscrições.")

        elif oficinaEscolhida == "criando e recriando emojis" and nomeIdentificado not in lNomeInscrito:
            of9+=1
            lOficinasRelacionadas = []
            lNomeInscrito.append[nomeIdentificado]
            lOficinaInscrita.append[oficinaEscolhida]
            lSerieInscrita.append[serieIdentificada]
            lRmInscrito.append[rmIdentificado] 
            print("Já foram feitas ", of9, " inscrições.")

        else:
            print("Você já está inscrito nessa oficina") 
    else:
        print("Aluno  não  cadastrado. Favor procurar a coordenação do Fundamental I")
        return



# fim variáveis e defs


# inicio codigo 
while True:
    print("Menu de opções")
    print("1 - Cadastrar alunos")
    print("2 - Fazer inscrições")
    print("3 - Listar inscrições")
    print("4 - Sair")


    xEscolha = int(input("Insira uma oção: "))
    while xEscolha < 1 or xEscolha > 4:
        print("Valor inválido, por favor insira uma opção utilizando apenas um número. (Exemplo: 1)")
        xEscolha = int(input("Insira uma oção: ")) 

    if xEscolha == 1 and bloqueio1 == 0:
        bloqueio1+= 1
        cadastro_usuario()
    elif xEscolha == 2:
        fazer_inscricoes()
    elif xEscolha == 3:
        print("EM CONSTRUÇÃO")
    else:
        break






