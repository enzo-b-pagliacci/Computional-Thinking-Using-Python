def cadastrar_numero(codigo, defeito):
    if(codigo not in mouses.keys()):
        mouses[codigo]=[]
    lista = mouses[codigo]
    if (5 in lista):
        mouses[codigo]=[5]
        lista = mouses[codigo]
        print("O mouse não possui defeitos \n")
    elif(4 in lista):
        mouses[codigo]=[4]
        lista = mouses[codigo]
        print("O mouse não pode ter mais defeitos pois está quebrado ou inutilizado \n")     
    elif (defeito in lista):
        print("Defeito já cadastrado \n")
    elif(defeito not in lista and len(lista) < 4):
        lista.append(defeito)
        mouses[codigo]=lista

def retira_defeito_opcoes(numero):
      for k, i in mouses.items():
        if k == numero:
            if 1 in i:
                listaValidaDef.pop(1, '')
            if 2 in i:
                listaValidaDef.pop(2, '')  
            if 3 in i:
                listaValidaDef.pop(3, '')   
            elif listaValidaDef == {}:
                print("Todas as opções de defeito foram utilizado") 
            return print(listaValidaDef.values())
#dicionário mouse
mouses = {}
    
#dicionário defeitos 
defeitos = {1: 'necessitam da esfera',
            2: 'necessitam de limpeza',
            3: 'necessitam troca do cabo ou conector',
            4: 'estão quebrados ou inutilizados',
            5: 'não tem defeito'}

print('\nLista de defeitos: ')
print("1 - Necessita da esfera\n2 - Necessita de limpeza\n3 - Necessita troca do cabo ou conector\n4 - Quebrado ou inutilizado\n5 - Não tem defeito")


while True:
    listaValidaDef = {1: "1 - Necessita de esfera", 2: "2 - Necessita de limpeza", 3: "3 - Necessita troca do cabo ou conector"}
    num_id = int(input("Digite o número de identificação do Mouse: "))
    if num_id == 0:
        break
    retira_defeito_opcoes(num_id)
    tp_def = int(input("Digite o tipo de defeito do mouse: "))
    while True:
        if 0 < tp_def < 6:
            cadastrar_numero(num_id, tp_def)
            break
        else:
            tp_def = int(input("Número de identificação de defeito invalido... Digite novamente: "))
            

for id, defeito in defeitos.items():
    print("\n--- Identificação dos mouses que {} ---".format(defeito))
    qt=0
    for mouse in mouses:
        if id in mouses[mouse]: 
            print("{}".format(mouse), end='  ')
            qt+=1
    if (qt == 1):
        print("\nTotal: 1 mouse.")
    elif (qt > 1):
        print("\nTotal: {} mouses.".format(qt))
    else:
        print("\nNenhum\nTotal: -----")

print("\n")    