ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

NAMES=input().split()

def Nombre_amour(name):
    S=0
    for lettre in name:
        S=S+ALPHABET.index(lettre)
    while S>=10:
        Q=str(S)
        S=0
        for n in Q:
            S=S+int(n)
    return S


OUT=[]
for name in NAMES:
    OUT.append(Nombre_amour(name))

OUT="{0} {1}".format(OUT[0],OUT[1])

print(OUT)
        
