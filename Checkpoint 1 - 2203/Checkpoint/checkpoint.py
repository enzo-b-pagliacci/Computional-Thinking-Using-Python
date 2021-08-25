xNome = input("Informe seu nome: ")
xSalF = float(input("Informe seu salário fixo: "))
sF = float(input("Informe o valor total vendido no setor feminino: "))
sM = float(input("Informe o valor total vendido no setor masculino: ")) 
sI = float(input("Informe o valor total vendido no setor infantil: ")) 
sB = float(input("Informe o valor total vendido no setor beleza: "))

cF = sF * 0.02
cM = sM * 0.02
cI = sI * 0.04
cB = sB * 0.06
cT = cF + cM + cI + cB
xT = xSalF + cT

print("Prezado(a)", xNome)
print("Seu salário fixo é de", xSalF, "reais e sua comissão referente ao mês vigente foi calculado em", cT, "reais.")
print("Total a receber:", xT, "reais")