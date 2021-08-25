num = int(input("Informe um numero: "))
chu = int(input("Chute um numero: "))
chutes = 0

if(chu != num):
    chutes += 1
    while(chu > num):
        print("Chute alto: ")
        input("chute denovo: ")
    while(chu < num):
        print("Chute baixo: ")
        input("chute denovo: ")
else:
    print("Parabens")
    print("A quantidade de chutes foi: ", chutes)
