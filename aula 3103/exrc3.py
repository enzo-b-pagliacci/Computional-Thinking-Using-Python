print("Insira o número da sua conta (apenas 3 digitos): ")
n1 = input("")
n2 = input("")
n3 = input("")

nConta = int(n1 + n2 + n3)
nContaInv = int(n3 + n2 + n1)

p1 = nConta + nContaInv
s1 = str(p1)


x1 = int(s1[0])
x2 = int(s1[1])
x3 = int(s1[2])

p2 =  x1 * 1 + x2 * 2 + x3 * 3

xRU = p2 % 10
print("O número verificador é: ", xRU)







