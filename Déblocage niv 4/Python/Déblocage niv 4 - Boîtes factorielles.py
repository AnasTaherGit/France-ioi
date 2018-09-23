from math import factorial
nbpetitpois=int(input())
i=1
while nbpetitpois//factorial(i)!=0:
    i+=1
print(i-1)
i-=1
Coef=[]
p=i

def findrest(x):
    global Coef
    for j in range(1,i):
        x%=factorial(p+1-j)
        
    x//=factorial(p-i+1)
    Coef.append(x)


for k in range(1,i+1):
    findrest(nbpetitpois)
    nbpetitpois-=Coef[k-1]*factorial(k)
    i-=1
M=str()
for coef in Coef:
    coef=str(coef)
    M=M+coef+" "

print(M)
