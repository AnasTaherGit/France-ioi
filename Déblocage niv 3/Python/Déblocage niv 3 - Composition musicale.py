M=input()
Music=[]
for x in M:
    Music.append(x)
i=0
while i<(len(Music)-1) :

    try:
        if Music[i]==Music[i+1]:    
            del Music[i+1]
            del Music[i]
            i=0
        else:
            i+=1
    except IndexError :
        break
    
M=str()
for j in Music:
    M=M+j
print(M)
