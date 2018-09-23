ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

TEXT=input().upper()
maxi=("",0)

for l in ALPHABET:
    k=TEXT.count(l)
    if k>maxi[1]:
        maxi=(l,k)

print(maxi[0])
