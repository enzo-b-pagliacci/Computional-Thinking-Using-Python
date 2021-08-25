mouses = []
while True:
    nIdenti = int(input("Insira a identificação do mouse: "))
    if nIdenti > 0 or nIdenti < 0:
        while nIdenti in mouses and nIdenti != 0:
            nIdenti = int(input("Mouse ja cadastrado. Insira a identificação do mouse: "))
        else:
            mouses.append(nIdenti)
            print("1•necessita da esfera")
            print("2•necessita de limpeza")
            print("3•necessita troca do cabo ou conector")
            print("4•quebrado ou inutilizado")
            tDefe = int(input())
            while tDefe > 4 or tDefe < 1:
                tDefe = int(input("Insira um valor valido: "))
            else:
                if tDefe == 1:
                    print("1")

                elif tDefe == 2:
                    print("2")

                elif tDefe == 3:
                    print("3")

                elif tDefe == 4:
                    print("4")
    else:
        print("resultado")    
        break
       
             

# mais parecido com oq eu ia tentar
# def ex4c():
#     def cadastrar_numero(valor, chave): #valor = 100, chave = 'numero'
#         while valor in mouses[chave]:
#             print('{} de mouse já cadastrado'.format(chave))
#             valor = int(input("Digite o número de identificação do Mouse: "))
#         mouses[chave].append(valor) #agora sim existirá
#     def cadastrar_defeito(valor, chave): #o valor é 1 e a chave = 'defeito'
#         while valor not in defeitos.keys():
#             print('{} não encontrado'.format(chave))
#             valor = int(input("Digite o tipo de defeito do mouse válido: "))
#         mouses[chave].append(valor)

#     #dicionário mouse - numero é a chave e o valor é uma lista que está vazia
#     mouses = {'numero': [],
#              'defeito': []}
#     #mouses = {'numero': [100], 'defeito': [1]}
#     #dicionário defeitos - a chave 1 tem o valor necessita da esfera, a chave 2 tem o valor necessita de limpeza e assim por diante
#     defeitos = {1: 'necessita da esfera',
#                 2: 'necessita de limpeza',
#                 3: 'necessita troca do cabo ou conector',
#                 4: 'quebrado ou inutilizado'}

#     print('Lista de defeitos: ')
#     for num, tipo in defeitos.items():
#         print(num, '-', tipo)

#     while True:
#         num_id = int(input("Digite o número de identificação do Mouse: "))
#         if num_id == 0:
#             break
#         cadastrar_numero(num_id, 'numero') #invocando cadastrar_numero mandando por parâmetro a identificação que é 100 e a palavra numero
#         tp_def = int(input("Digite o tipo de defeito do mouse: "))
#         cadastrar_defeito(tp_def, 'defeito') #invocando cadastrar_defeito mandando por parâmetro o tipo de defeito que no caso é 1 e a palavra defeito
#     qt_mouse = len(mouses['numero'])
#     print('Quantidade de mouses: {}'.format(qt_mouse))
#     print("Situação \t\t\t\t\t\t\t\t\tQuantidade\t\t\t\tPercentual")
#     for num, tipo in defeitos.items():
#         print("{} - {:<47} {:<20} {:<2}%".format(num, tipo, mouses['defeito'].count(num),
#                                                  ((mouses['defeito'].count(num)) / qt_mouse) * 100))