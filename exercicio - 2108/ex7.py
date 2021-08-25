listaA = [9,8,7,1,6,2,4,3,1,6]
listaB = [8,6,4,9,5,3,1,3,6,4]
conja = set(listaA)
conjb = set(listaB)

# a)
print(conja.difference(conjb))

# b)
re = []
for i in conja:
    if (listaA.count(i) > 1):
        re.append(i)
print("Os numeros que se repetem são: ", re)     

# c)
rb = []
for i in conjb:
    if (listaB.count(i) > 1):
        rb.append(i)
print("Os numeros que se repetem são: ", rb)  
        
# d)
rd = []
for l in listaA:
    rd.append(l)
for m in listaB:
    rd.append(m)    
print(rd) 

# e)
rd = set(rd)
print(rd)




