P=int(input())
N=list(map(int,input().split()))

O=int(input())
for op in range(0,O):
   C=list(map(int,input().split()))
   N[C[0]-1]+=C[1]
   
print(' '.join(list(map(str,N))))
