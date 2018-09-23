IN=[]
nblivre=int(input())
for i in range(0,nblivre):
    IN.append(input())

def treat(e):
    e=e.split()
    return "".join(e).upper()

TR=list(map(treat,IN))


OUT=[]
for i in TR:
    if i==i[::-1]:
        OUT.append(IN[TR.index(i)])

for i in OUT:
    print(i)

    
    
