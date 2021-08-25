n = int(input("Verificar se numero é primo: "))

for count in range(2,n):
    if (n % count != 0):
        print(str(n) + " é primo.")
        break
    else:
        print("não é primo")
        break
 

