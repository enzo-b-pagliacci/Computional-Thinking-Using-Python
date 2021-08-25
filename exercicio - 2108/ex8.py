def cadastrar(numero,defeito): 
    if defeito == 1:
        mouses[numero] = ['1•necessita da esfera']
        defs["1•necessita da esfera"].append(1)   
    elif defeito == 2:
        mouses[numero] = ['2•necessita de limpeza']
        defs["2•necessita de limpeza"].append(1)
    elif defeito == 3:
        mouses[numero] = ['3•necessita troca do cabo ou conector']
        defs["3•necessita troca do cabo ou conector"].append(1)
    elif defeito == 4:
        mouses[numero] = ['4•quebrado ou inutilizado']
        defs["4•quebrado ou inutilizado"].append(1)
    elif defeito == 5:
        mouses[numero] = ['5•sem defeito']
        defs["5•sem defeito"].append(1)
        
def cadastrar_mais_defeitos(numero):
    print("1•necessita da esfera")
    print("2•necessita de limpeza")
    print("3•necessita troca do cabo ou conector")
    print("4•quebrado ou inutilizado") 
    defeito = int(input("Insira o outro defeito do mouse: ")) 
    while defeito > 4 or defeito < 1:
        defeito = int(input("Valor inválido. Insira o outro defeito do mouse: ")) 
    if defeito == 1:
        if '1•necessita da esfera' in mouses[numero]:
            print("Este defeito já está cadastrado")
        else:
            mouses[numero].append('1•necessita da esfera')
            defs["1•necessita da esfera"].append(1)
    if defeito == 2:
        if '2•necessita de limpeza' in mouses[numero]:
            print("Este defeito já está cadastrado")
        else:
            mouses[numero].append('2•necessita de limpeza')
            defs["2•necessita de limpeza"].append(1)
    elif defeito == 3:
        if '3•necessita troca do cabo ou conector' in mouses[numero]:
            print("Este defeito já está cadastrado")
        else:
            mouses[numero].append('3•necessita troca do cabo ou conector')
            defs["3•necessita troca do cabo ou conector"].append(1)
    elif defeito == 4:
        if '4•quebrado ou inutilizado' in mouses[numero]:
            print("Este defeito já está cadastrado")
        else:
            mouses[numero].append('4•quebrado ou inutilizado')
            defs["4•quebrado ou inutilizado"].append(1)

defs = {'1•necessita da esfera': [], 
        '2•necessita de limpeza': [],
        '3•necessita troca do cabo ou conector': [],
        '4•quebrado ou inutilizado': [],
        '5•sem defeito': []}
mouses = dict ()


def listagemEOrdenagem(lista, defeito):
  keys = []
  for k, v in mouses.items():
      for i in v:
         if i == defeito:
            keys.append(k)
  keys.sort()
  lista.append(keys)

    


while True:
    nIdenti = int(input("Insira a identificação do mouse: "))
    if nIdenti > 0 or nIdenti < 0:
        while nIdenti in list(mouses.keys()) and nIdenti != 0:
            nIdenti = int(input("Mouse ja cadastrado. Insira a identificação do mouse: "))
            if nIdenti == 0:
                print("Ok, identificação de mouse cancelada... Pressione 0 mais uma vez para finalizar o programa")
                break
                
        else:
            print("1•necessita da esfera")
            print("2•necessita de limpeza")
            print("3•necessita troca do cabo ou conector")
            print("4•quebrado ou inutilizado")
            print("5•sem defeito")
            tDefe = int(input())
            while tDefe > 5 or tDefe < 1:
                tDefe = int(input("Insira um valor valido: "))
            else:
                cadastrar(nIdenti,tDefe)
                if tDefe < 5 and tDefe > 0:
                    sN = input("Este mouse tem mais algum defeito? Digite 'S' para sim e 'N' para não: ").upper()
                    while sN != 'S' and sN !='N':
                        sN = input("Valor inválido? Digite 'S' para sim e 'N' para não: ").upper()               
                    
                    while sN == 'S':              
                        cadastrar_mais_defeitos(nIdenti)
                        sN = input("Este mouse tem mais algum defeito? Digite 'S' para sim e 'N' para não: ").upper()
                        if sN == 'N':
                            break              

    else:
        print("----Identificação dos mouses que estão sem defeito ----") 
        semDef = []
        listagemEOrdenagem(semDef,'5•sem defeito')
        if semDef == [[]]:
            print("Nenhum")
            print("Total: -----")
        else:
            print(semDef)
            print("Total: ", len(defs["5•sem defeito"])) 
        print("\n")



        print("---- Identificação dos mouses que necessitam de esfera ----")
        esferaDef = []
        listagemEOrdenagem(esferaDef,'1•necessita da esfera')
        if esferaDef == [[]]:
            print("Nenhum")
            print("Total: -----")
        else:
            print(esferaDef)
            print("Total: ", len(defs["1•necessita da esfera"]))
        print("\n")



        print("---- Identificação dos mouses que necessitam de limpeza ----")
        limpezaDef = []
        listagemEOrdenagem(limpezaDef,'2•necessita de limpeza')
        if limpezaDef == [[]]:
            print("Nenhum")
            print("Total: -----")
        else:
            print(limpezaDef)
            print("Total: ", len(defs["2•necessita de limpeza"]))
        print("\n")



        print("---- Identificação dos mouses que necessitam troca de cabo ou conector ----")
        caboDef = []
        listagemEOrdenagem(caboDef,'3•necessita troca do cabo ou conector')
        if caboDef == [[]]:
            print("Nenhum")
            print("Total: -----")
        else:
            print(caboDef)
            print("Total: ", len(defs["3•necessita troca do cabo ou conector"]))
        print("\n")



        print("---- Identificação dos mouses que estão quebrados ou inutilizados ----")
        quebraDef = []
        listagemEOrdenagem(quebraDef,'4•quebrado ou inutilizado')
        if quebraDef == [[]]:
            print("Nenhum")
            print("Total: -----")
        else:
            print(quebraDef)
            print("Total: ", len(defs["4•quebrado ou inutilizado"]))
        break
       
             

