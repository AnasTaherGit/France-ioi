p="0"
S=0
while 1:
   try:
      p=input()
      assert p!=''
      p=p.split()
      for n in p:
         S+=int(n)
   except:
      break
print(S)
