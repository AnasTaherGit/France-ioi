nbgrenouilles=int(input())
nbtours=int(input())
distance=[0]*nbgrenouilles
tete=[0]*nbgrenouilles

for i in range(0,nbtours):
    q=input().split()
    if i!=nbtours-1:
        distance[int(q[0])-1]+=int(q[1])
        m=max(x for x in distance)
        if distance.count(m)==1:
            k=distance.index(m)
            tete[k]+=1
        else :
            pass

    
print(tete.index(max(x for x in tete))+1)

