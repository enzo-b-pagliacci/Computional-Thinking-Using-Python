xDest = input("Qual o destino (Norte / Nordeste / Centro-Oeste)?  ").lower()
if (xDest == "nordeste" or xDest == "norte" or xDest == "centro-oeste"):
    xIV = input("Diga se você fará uma viagem 'ida' ou 'ida e volta': ").lower()
    if (xIV == "ida" or xIV == "ida e volta"):
        if (xDest == "norte" and xIV == "ida"):
            print("O valor da passagem será: R$ 280,00")
        elif (xDest == "nordeste" and xIV == "ida"):
            print("O valor da passagem será: R$ 380,00")
        elif (xDest == "centro-oeste" and xIV == "ida"):
            print("O valor da passagem será: R$ 620,00")
        elif (xDest == "norte" and xIV == "ida e volta"):
            print("O valor da passagem será: R$ 400,00")
        elif (xDest == "nordeste" and xIV == "ida e volta"):
            print("O valor da passagem será: R$ 628,00")
        elif (xDest == "centro-oeste" and xIV == "ida e volta"):
            print("O valor da passagem será: R$ 1100,00")
    else: 
        print("insira um valor valido: 'Ida' ou 'Ida e volta'")
else:
    print("Informe um destino válido: 'Norte', 'Nordeste' ou 'Centro-Oeste'")
 
    
               
        

