tV = []
pC = []
nV = []
vR = []

for i in range (0, 2):
    tV.append(float(input("Insira o total de vendas referente ao vendedor: ")))
    pC.append(float(input("Insira o percentual de comissão referente ao vendedor: ")))
    nV.append(input("Insira o nome referente ao vendedor: "))
    vR.append(str(tV[i] * (pC[i]/100)))

for i in range (0, 2):
    print("Nome: " + nV[i] + "; Valor a receber referente à comissão: " + vR[i])

print(sum(tV))
print("O maior valor a receber é: " + (max(vR)) + "; Nome do vendedor é: " + (n for i in range(max(vR)) = nV[n]) )
print("O maior valor a receber é: " + (min(vR)) + "; Nome do vendedor é: " + )