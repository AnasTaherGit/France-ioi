livrelire=[""]*int(input())
for i in range(0,len(livrelire)):
   livrelire[i]=input()


livrelu=livrelire[0]
print(livrelu)
for i in range(1,len(livrelire)):
   if livrelu<livrelire[i]:
      livrelu=livrelire[i]
      print(livrelu)
