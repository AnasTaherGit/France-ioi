ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

TEXT=input().upper()
S=0
for l in TEXT:
    if l.isalpha():
        S+=1
    
for l in ALPHABET:
    k=TEXT.count(l)
    print(k/S)

