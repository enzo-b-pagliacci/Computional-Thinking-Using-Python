n = int(input("Insira o número de termos da sequencia de Fibonacci: "))
cont = 1
anterior = 1


print(1)
print(1)
for i in range (1, n-1):
    cont = anterior + cont 
    anterior = cont - anterior
    print(cont)
