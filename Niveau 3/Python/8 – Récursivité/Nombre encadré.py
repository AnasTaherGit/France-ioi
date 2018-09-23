def Encadre(m,n):
   
   if n==0: return m
   
   else: return '['+Encadre(m,n-1)+']'
   
m,n=input().split()

print(Encadre(m,int(n)))