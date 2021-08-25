desconto = float(0)
qtdP = int(input("Quantidade de pratos principais: "))
while qtdP <= 0:
    print("Número de pratos principais inválido. Digite novamente.")
    qtdP = int(input("Quantidade de pratos principais: "))
else:
    if qtdP > 3:
        desconto = desconto + 0.04
    vTN = float(input("Valor da nota: "))
while vTN <= 0:
    print("Valor da nota inválido. Digite novamente.")
    vTN = float(input("Valor da nota: "))
else:
    if vTN > 500:
        desconto = desconto + 0.06    
    cup = input("Tem cupom? ")
if cup == "S":
    nomeCup = input("Digite o cupom: ")
    while cup == "S" and (nomeCup !="BORALA10" and nomeCup !="BORALA05"):
        print("Cupom inválido. Digite novamente.")
        cup = input("Tem cupom? ")
        if cup == "S":
            nomeCup = input("Digite o cupom: ")           
    if cup == "N":   
        print("Ok, sem cupom")
        pvR = input("É a primeira vez que visita o restaurante? ")
        while pvR != "S" and pvR != "N":
            print("Valor inválido. Digite novamente ('S' ou 'N')")
            pvR = input("É a primeira vez que visita o restaurante?")
        else:
            if pvR == "S":
                desconto = desconto + 0.05
                print("Valor total da nota fiscal: ", vTN)
                vTCD = vTN - vTN * desconto 
                print("Valor total da nota com desconto: ", vTCD)
                pQ = int(input("Quantas pessoas realizaram a compra? "))
                racharConta = input("Rachar conta? ")
                while racharConta != "S" and racharConta != "N":
                    print("Valor inválido. Digite novamente ('S' ou 'N')")
                    racharConta = input("Rachar conta? ")
                else:
                    if racharConta == "S":
                        CRachada = vTCD / pQ
                        print("Número de pessoas: ", pQ)
                        print("Total por pessoa: ", CRachada)
                    elif racharConta == "N":
                        print("Ok, valor total da nota fiscal: ", vTN)
                        print("valor total da nota com desconto: ", vTCD)
            elif pvR == "N":
        
                print("Valor total da nota fiscal: ", vTN)
                vTCD = vTN - vTN * desconto 
                print("Valor total da nota com desconto: ", vTCD)
                pQ = int(input("Quantas pessoas realizaram a compra? "))
                racharConta = input("Rachar conta? ")
                while racharConta != "S" and racharConta != "N":
                    print("Valor inválido. Digite novamente ('S' ou 'N')")
                    racharConta = input("Rachar conta? ")
                else:
                    if racharConta == "S":
                        CRachada = vTCD / pQ
                        print("Número de pessoas: ", pQ)
                        print("Total por pessoa: ", CRachada)
                    elif racharConta == "N":
                        print("Ok, valor total da nota fiscal: ", vTN)
                        print("valor total da nota com desconto: ", vTCD)
            else:
                ("valor inválido")
    elif nomeCup == "BORALA10":
        desconto = desconto + 0.10  
        pvR = input("É a primeira vez que visita o restaurante? ")
        while pvR != "S" and pvR != "N":
            print("Valor inválido. Digite novamente ('S' ou 'N')")
            pvR = input("É a primeira vez que visita o restaurante?")
        else:
            if pvR == "S":
                desconto = desconto + 0.05
                print("Valor total da nota fiscal: ", vTN)
                vTCD = vTN - vTN * desconto 
                print("Valor total da nota com desconto: ", vTCD)
                pQ = int(input("Quantas pessoas realizaram a compra? "))
                racharConta = input("Rachar conta? ")
                while racharConta != "S" and racharConta != "N":
                    print("Valor inválido. Digite novamente ('S' ou 'N')")
                    racharConta = input("Rachar conta? ")
                else:
                    if racharConta == "S":
                        CRachada = vTCD / pQ
                        print("Número de pessoas: ", pQ)
                        print("Total por pessoa: ", CRachada)
                    elif racharConta == "N":
                        print("Ok, valor total da nota fiscal: ", vTN)
                        print("valor total da nota com desconto: ", vTCD)
            elif pvR == "N":
        
                print("Valor total da nota fiscal: ", vTN)
                vTCD = vTN - vTN * desconto 
                print("Valor total da nota com desconto: ", vTCD)
                pQ = int(input("Quantas pessoas realizaram a compra? "))
                racharConta = input("Rachar conta? ")
                while racharConta != "S" and racharConta != "N":
                    print("Valor inválido. Digite novamente ('S' ou 'N')")
                    racharConta = input("Rachar conta? ")
                else:
                    if racharConta == "S":
                        CRachada = vTCD / pQ
                        print("Número de pessoas: ", pQ)
                        print("Total por pessoa: ", CRachada)
                    elif racharConta == "N":
                        print("Ok, valor total da nota fiscal: ", vTN)
                        print("valor total da nota com desconto: ", vTCD)
            else:
                ("valor inválido")
    elif nomeCup == "BORALA05":
        desconto = desconto + 0.05  
        pvR = input("É a primeira vez que visita o restaurante? ")
        while pvR != "S" and pvR != "N":
            print("Valor inválido. Digite novamente ('S' ou 'N')")
            pvR = input("É a primeira vez que visita o restaurante?")
        else:
            if pvR == "S":
                desconto = desconto + 0.05
                print("Valor total da nota fiscal: ", vTN)
                vTCD = vTN - vTN * desconto 
                print("Valor total da nota com desconto: ", vTCD)
                pQ = int(input("Quantas pessoas realizaram a compra? "))
                racharConta = input("Rachar conta? ")
                while racharConta != "S" and racharConta != "N":
                    print("Valor inválido. Digite novamente ('S' ou 'N')")
                    racharConta = input("Rachar conta? ")
                else:
                    if racharConta == "S":
                        CRachada = vTCD / pQ
                        print("Número de pessoas: ", pQ)
                        print("Total por pessoa: ", CRachada)
                    elif racharConta == "N":
                        print("Ok, valor total da nota fiscal: ", vTN)
                        print("valor total da nota com desconto: ", vTCD)
            elif pvR == "N":
        
                print("Valor total da nota fiscal: ", vTN)
                vTCD = vTN - vTN * desconto 
                print("Valor total da nota com desconto: ", vTCD)
                pQ = int(input("Quantas pessoas realizaram a compra? "))
                racharConta = input("Rachar conta? ")
                while racharConta != "S" and racharConta != "N":
                    print("Valor inválido. Digite novamente ('S' ou 'N')")
                    racharConta = input("Rachar conta? ")
                else:
                    if racharConta == "S":
                        CRachada = vTCD / pQ
                        print("Número de pessoas: ", pQ)
                        print("Total por pessoa: ", CRachada)
                    elif racharConta == "N":
                        print("Ok, valor total da nota fiscal: ", vTN)
                        print("valor total da nota com desconto: ", vTCD)
            else:
                ("valor inválido")
    else:
        print("valor inválido")    
elif cup == "N":             
    pvR = input("É a primeira vez que visita o restaurante? ")
    while pvR != "S" and pvR != "N":
        print("Valor inválido. Digite novamente ('S' ou 'N')")
        pvR = input("É a primeira vez que visita o restaurante?")
    else:
        if pvR == "S":
            desconto = desconto + 0.05
            print("Valor total da nota fiscal: ", vTN)
            vTCD = vTN - vTN * desconto 
            print("Valor total da nota com desconto: ", vTCD)
            pQ = int(input("Quantas pessoas realizaram a compra? "))
            racharConta = input("Rachar conta? ")
            while racharConta != "S" and racharConta != "N":
                print("Valor inválido. Digite novamente ('S' ou 'N')")
                racharConta = input("Rachar conta? ")
            else:
                if racharConta == "S":
                    CRachada = vTCD / pQ
                    print("Número de pessoas: ", pQ)
                    print("Total por pessoa: ", CRachada)
                elif racharConta == "N":
                    print("Ok, valor total da nota fiscal: ", vTN)
                    print("valor total da nota com desconto: ", vTCD)
        elif pvR == "N":
    
            print("Valor total da nota fiscal: ", vTN)
            vTCD = vTN - vTN * desconto 
            print("Valor total da nota com desconto: ", vTCD)
            pQ = int(input("Quantas pessoas realizaram a compra? "))
            racharConta = input("Rachar conta? ")
            while racharConta != "S" and racharConta != "N":
                print("Valor inválido. Digite novamente ('S' ou 'N')")
                racharConta = input("Rachar conta? ")
            else:
                if racharConta == "S":
                    CRachada = vTCD / pQ
                    print("Número de pessoas: ", pQ)
                    print("Total por pessoa: ", CRachada)
                elif racharConta == "N":
                    print("Ok, valor total da nota fiscal: ", vTN)
                    print("valor total da nota com desconto: ", vTCD)
        else:
            ("valor inválido")
else:
    print("Valor inválido")

    
    










    
    








