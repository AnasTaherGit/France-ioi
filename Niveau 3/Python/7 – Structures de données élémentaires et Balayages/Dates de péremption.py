O=int(input())
P=[]
for op in range(0,O):
   c=list(map(int,input().split()))
   if c[0]>=0:
      for loop in range(0,c[0]):
         P.append(c[1])
   else:
      for loop in range(0,abs(c[0])):
         P.pop()
print(min(P)) 