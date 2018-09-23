chess=[]
for i in range(0,8):
    k=input()
    chess.append(k)

def cavalier():
    chevalier=[]
    for i in range(0,len(chess)):
        for j in range(0,len(chess)):
            if chess[i][j]=="C":
                chevalier.append((i,j))
    return chevalier

for l in cavalier():
#1
    try:
        if chess[l[0]-2][l[1]-1].islower():
            print("yes")
            break

    except :
        pass
#2    
    try:
        if chess[l[0]-2][l[1]+1].islower():
            print("yes")
            break

    except :
        pass    
#3
    try:
        if chess[l[0]-1][l[1]+2].islower():
            print("yes")
            break

    except :
        pass
#4
    try:
        if chess[l[0]+1][l[1]+2].islower():
            print("yes")
            break

    except :
        pass
#5
    try:
        if chess[l[0]+2][l[1]+1].islower():
            print("yes")
            break

    except :
        pass

#6
    try:
        if chess[l[0]+2][l[1]-1].islower():
            print("yes")
            break

    except :
        pass

#7
    try:
        if chess[l[0]+1][l[1]-2].islower():
            print("yes")
            break

    except :
        pass
#8
    try:
        if chess[l[0]-1][l[1]+2].islower():
            print("yes")
            break

    except :
        pass
    if l==cavalier()[-1]:
        print("no")
        
