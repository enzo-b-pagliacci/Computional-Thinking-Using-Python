
numeros = []
i = 0
while i < 20:
    n = int(input("Insira um número inteiro: "))
    numeros.append(n)
    i += 1
print(max(numeros))
print(min(numeros))