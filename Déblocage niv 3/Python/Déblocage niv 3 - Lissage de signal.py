nbMesure=int(input())
diffMax=float(input())
mesures=[float(input()) for i in range(0,nbMesure)]
i=0
def vérification(Mesure):
    for j in range(0,len(Mesure)-1):
        if abs(Mesure[j]-Mesure[j+1])>=diffMax:
            return True
            break
    return False

def lissage():
    global mesures
    l=[]
    l.append(mesures[0])
    for j in range(1,len(mesures)-1):
        l.append((mesures[j-1]+mesures[j+1])/2)
    l.append(mesures[-1])
    mesures=l

while vérification(mesures):
    lissage()
    i+=1
print(i)
