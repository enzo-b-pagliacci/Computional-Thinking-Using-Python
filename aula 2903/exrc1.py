vSB = float(input("Informe seu salário bruto: "))
vP = float(input("Informe o valor da prestação: "))

if (vSB > 0 and vP > 0):
    limite = vSB * 0.30

    if (vP <= limite):
        print("O empréstimo pode ser concedido")

    else :
        print("O empréstimo não pode ser concedido")

else :
    print("Informe um salário bruto e o valor da prestação maior que 0")