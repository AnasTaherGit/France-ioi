dim=input().split()

grid=[]
for i in range(0,int(dim[0])):
   grid.append(['.']*int(dim[1]))
  
rects=[""]*int(input())
for i in range(0,len(rects)):
   print(i) 
   rects[i]=input().split()

print(rects)
for rect in rects:
    for i in range(int(rect[0]),int(rect[2])+1):
        for j in range(int(rect[1]),int(rect[3])+1):
            grid[i][j]=rect[4]

for i in range(0,int(dim[0])):
    print("".join(grid[i]))
    
