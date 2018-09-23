ALPHA="abcdefghijklmnopqrstuvwxyz"

def déchifrage_lettre(l):
    if l.isalpha():
        if l.isupper():
            l=l.lower()
            #---------- Déchiffrage -----------
            return clé[ALPHA.index(l)].upper()
            #----------  Chiffrage ------------
            #return ALPHA[clé.index(l)].upper()
        else:
            #---------- Déchiffrage -----------
            return clé[ALPHA.index(l)]
            #----------  Chiffrage ------------
            #return ALPHA[clé.index(l)]
    else:
        return l

def déchifrage_mot(m):
    return ("".join([déchifrage_lettre(l) for l in m]))

def déchifrage_texte(t):
    return (" ".join(list(map(déchifrage_mot,t.split()))))

clé=input()

texte=input()

print(déchifrage_texte(texte))


    
    
    
