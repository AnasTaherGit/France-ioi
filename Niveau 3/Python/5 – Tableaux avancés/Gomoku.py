Gomuko=[]
dim=int(input())
flag=False
for l in range(0,dim):
    Gomuko.append(input().split())

for i in range(0,dim-1):
    for j in range(0,dim-1):
#--------- Parcours en ligne -------------
        try:
            if Gomuko[i][j]==Gomuko[i][j+1]==Gomuko[i][j+2]==Gomuko[i][j+3]==Gomuko[i][j+4] and (Gomuko[i][j]=="1" or Gomuko[i][j]=="2"):
                if Gomuko[i][j]=="1":
                    flag=True
                    print("1")
                    break
                elif Gomuko[i][j]=="2":
                    flag=True
                    print("2")
                    break
        except:
            pass
#--------- Parcours en colonnes ----------
        try:
            if Gomuko[i][j]==Gomuko[i+1][j]==Gomuko[i+2][j]==Gomuko[i+3][j]==Gomuko[i+4][j] and (Gomuko[i][j]=="1" or Gomuko[i][j]=="2"):
                if Gomuko[i][j]=="1":
                    flag=True
                    print("1")
                    break
                elif Gomuko[i][j]=="2":
                    flag=True
                    print("2")
                    break
        except:
            pass

#--------- Parcours en diagonale_direct ---------
        try:
            if Gomuko[i][j]==Gomuko[i+1][j+1]==Gomuko[i+2][j+2]==Gomuko[i+3][j+3]==Gomuko[i+4][j+4] and (Gomuko[i][j]=="1" or Gomuko[i][j]=="2"):
                if Gomuko[i][j]=="1":
                    flag=True
                    print("1")
                    break
                elif Gomuko[i][j]=="2":
                    flag=True
                    print("2")
                    break
        except:
            pass
#---------- Parcours en diagonale_inverse ----------
        try:
            if Gomuko[i][dim-j-1]==Gomuko[i+1][dim-j-2]==Gomuko[i+2][dim-j-3]==Gomuko[i+3][dim-j-4]==Gomuko[i][dim-j-5] and (Gomuko[i][dim-j-1]=="1" or Gomuko[i][dim-j-1]=="2"):
                if Gomuko[i][dim-j-1]=="1":
                    flag=True
                    print("1")
                    break
                elif Gomuko[i][dim-j-1]=="2":
                    flag=True
                    print("2")
                    break
        except:
            pass
        
    if flag==True:
        break
    if i==dim-1:
        print(0)
