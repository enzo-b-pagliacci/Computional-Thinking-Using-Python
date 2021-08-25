João e Matheus Pismel

'''
1) Faça um programa em Python que receba do usuário sete números inteiros, calcule e mostre:
a) Os números múltiplos de 2;
b) Os números múltiplos de 3;
'''

Lista = []
Multiplo2 = []
Multiplo3 = []

for i in range(0,7):
    Lista.append(int(input("Digite os números: ")))
if Lista[i] % 2 == 0:
        Multiplo2.append(Lista[i])
if Lista[i] % 3 == 0:
        Multiplo3.append(Lista[i])

print("Multiplos de 2", Multiplo2)
print("Multiplos de 3", Multiplo3)