acro=input()
livres=[""]*int(input())
for i in range(0,len(livres)):
   livres[i]=(input().upper()).split()

def k(x):
   if len(x)==len(acro) and all([acro[i]==x[i][0] for i in range(0,len(acro))]):
      return True
   return False


livres=list(filter(k,livres))

def W(x):
    for l in x:
        l=l.lower()
        l[0]=l[0].upper()
        
livres=list(map(W,livres))

for i in range(0,len(livres)):
    livre=livres[i][0]
    for j in range(1,len(acro)):
        livre=livre+livres[i][j]

    livres[i]=livre

for l in livres :
    print(l)
    
