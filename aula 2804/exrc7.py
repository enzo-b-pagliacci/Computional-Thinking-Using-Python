num = int(input("Informe um numero: "))
chu = int()
chutes = 0
while (chu != num):
    chu = int(input("Chute um numero: "))
    chutes += 1
    if (chu > num):
        print("Chute alto: ")
    elif (chu < num):
        print("Chute baixo: ")

print("Parabens")
print("A quantidade de chutes foi: ", chutes)