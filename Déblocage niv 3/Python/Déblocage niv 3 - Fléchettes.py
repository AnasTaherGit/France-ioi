n=int(input())
cible=[]
for x in range(0,n):
    cible.append([""]*n)

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for j in range(0,n):
    for i in range(0,n):
        if i<j :
            cible[j][i]=alphabet[i]
        if i>=j :
            cible[j][i]=alphabet[j]

for j in range(0,n):
    for i in range(0,n-1):
        cible[j].append(cible[j][n-i-2])
        
for j in range(0,n-1):
    cible.append(cible[n-2-j])

    
#print(cible)

# ----------------------- Affichage ----------------------

for j in range(0,2*n-1):
    matrice=cible[j][0]
    for i in range(1,2*n-1):
        matrice=matrice+cible[j][i]
        
    print(matrice)

#os.system("pause")
