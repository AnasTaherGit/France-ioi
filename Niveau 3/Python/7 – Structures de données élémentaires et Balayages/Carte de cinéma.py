def tricheur(seq):
   visited=set()
   for e in seq:
      if e in visited:
         return e
      else:
         visited.add(e)
   return -1
   
n=input()
seq=list(map(int,input().split()))
print(tricheur(seq))