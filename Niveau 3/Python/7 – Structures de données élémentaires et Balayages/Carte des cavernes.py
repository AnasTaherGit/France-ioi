def is_valide(s):
   opened=0
   closed=0
   
   for c in s:
      if c=='(':
         opened+=1
      elif c==')':
         closed+=1
      if opened<closed :
         return 0
   if opened==closed:
      return 1
   else:
      return 0
      
n=input()
s=input()
print(is_valide(s))