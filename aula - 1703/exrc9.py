vA=int(input("Quantos votos o candidato A teve? "))
vB=int(input("Quantos votos o candidato B teve? "))
vC=int(input("Quantos votos o candidato C teve? "))
xB=int(input("Quantos votos brancos tiveram? "))
xN=int(input("Quantos votos nulos tiveram? "))

nTE = vA + vB + vC + xB + xN

pA = (vA * 100) / nTE
pB = (vB * 100) / nTE
pC = (vC * 100) / nTE
pB = (xB * 100) / nTE
pN = (xN * 100) / nTE


print("O pertencual de eleitores do candidato A é: ", pA, "e do B é: ", pB, "e do C é: ", pC)
print("O percentual de votos brancos é: ", pB)
print("O percentual de votos nulos é: ", pN)