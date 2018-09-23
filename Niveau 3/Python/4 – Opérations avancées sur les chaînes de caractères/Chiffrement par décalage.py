ALPHA="abcdefghijklmnopqrstuvwxyz"

def déchifrage_lettre(l):
    if l.isalpha():
        if l.isupper():
            l=l.lower()
            #---------- Déchiffrage -----------
            #return clé[ALPHA.index(l)].upper()
            #----------  Chiffrage ------------
            return ALPHA[(ALPHA.index(l)-clé)%26].upper()
        else:
            #---------- Déchiffrage -----------
            #return clé[ALPHA.index(l)]
            #----------  Chiffrage ------------
            return ALPHA[(ALPHA.index(l)-clé)%26]
    else:
        return l

def déchifrage_mot(m):
    return ("".join([déchifrage_lettre(l) for l in m]))

def déchifrage_texte(t):
    return (" ".join(list(map(déchifrage_mot,t.split()))))

Nbpages=int(input())

textes=[]
for t in range(2,Nbpages+1):
   textes.append(input())
   
X=2
for page in textes:
      print(X)  
      if X%2==0:
         clé=X*3
         print(déchifrage_texte(page))
         X+=1
      else:
         clé=-5*X
         print(déchifrage_texte(page))
         X+=1
