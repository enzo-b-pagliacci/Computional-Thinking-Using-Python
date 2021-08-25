print("informe o valor de um boleto, o percentual de juros cobrado e o numero de dias em atraso: ")
vB=float(input(""))
pJ=float(input(""))
nA=float(input(""))

xR = vB + (vB * (pJ/100)) *nA

print("O valor a ser pago será: ", xR)