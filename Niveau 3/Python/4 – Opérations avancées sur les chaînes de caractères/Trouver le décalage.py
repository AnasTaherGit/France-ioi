ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

texte=input()
Search=texte.upper()
maxi=("",0)

for l in ALPHABET:
    k=Search.count(l)
    if k>maxi[1]:
        maxi=(l,k)
  

ALPHA="abcdefghijklmnopqrstuvwxyz"

def déchifrage_lettre(l):
    if l.isalpha():
        if l.isupper():
            l=l.lower()
            #---------- Déchiffrage -----------
            return ALPHA[(ALPHA.index(l)-clé)%26].upper()

        else:
            #---------- Déchiffrage -----------
            return ALPHA[(ALPHA.index(l)-clé)%26]

    else:
        return l

def déchifrage_mot(m):
    return ("".join([déchifrage_lettre(l) for l in m]))

def déchifrage_texte(t):
    return (" ".join(list(map(déchifrage_mot,t.split()))))


clé=(ALPHA.index(maxi[0].lower())-4)%26

print(déchifrage_texte(texte))
