def zero(n):

   if n==0 : return '0'
   else : return '('+zero(n-1)+' + '+zero(n-1)+')'
   
n=int(input())
print("0 = "+zero(n))