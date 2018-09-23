k=input()
N=list(map(int,input().split()))
M=list(map(int,input().split()))
I=[]
N.append(10**9)
for m in M:
    for i in range(len(N)):
        if i==0:
            if m<=N[i]:
                N.insert(0,m)
                I.append(0)

                break     
        else:
            if N[i-1]<m<=N[i]:
                N.insert(i,m)
                I.append(i)
                
                break

del N[-1]

print(' '.join(list(map(str,I))))
print(' '.join(list(map(str,N))))
