def is_unique(t,n):
    t=t.split()
    for i in t:
        if t.count(str(i))>1 or int(i)>n**2 or int(i)<=0:
            return False

    return True

#----------------------------------------- Parcours en ligne ----------------------------------------------------------------
def ligne_sum(l):
    b=[sum(l[i]) for i in range(0,len(l))]
    if len(b)==b.count(sum(l[0])) :
        return (True,sum(l[0]))
    else:
        return (False,-1)

#----------------------------------------- Parcours en colonnes -------------------------------------------------------------
def col(j,l):
    return [l[i][j] for i in range (0,len(l))]

def colonnes_sum(l):
    b=[ sum(col(j,l)) for j in range(0,len(l)) ]
    if len(b)==b.count(sum(col(0,l))) :
        return (True,sum(col(0,l)))
    else:
        return (False,-1)

#---------------------------------------- Parcours en diagonales -------------------------------------------------------------

def diagonale_direct(l):
    return [l[i][i] for i in range(0,len(l))]

def diagonale_inverse(l):
    return [l[i][len(l)-i-1] for i in range(0,len(l))]

def diagonale_sum(l):
    if sum(diagonale_direct(l))==sum(diagonale_inverse(l)):
        return (True,sum(diagonale_direct(l)))
    else :
        return (False,-1)

#------------------------------------  Programme principale ------------------------------

def main():
    N=int(input())
    l=[]
    for i in range(0,N):
        k=input()
        l.append(k)
    t=" ".join(l)
    for m in range(0,N):
        l[m]=l[m].split()
        l[m]=list(map(int,l[m]))
        
    if diagonale_sum(l)[0] and ligne_sum(l)[0] and colonnes_sum(l)[0] and diagonale_sum(l)[1]==ligne_sum(l)[1]==colonnes_sum(l)[1] and is_unique(t,N) :
        print("yes")

    else: print("no")

main()

                                                                        
        
        
           
           
