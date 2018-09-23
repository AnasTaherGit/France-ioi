nbBacs = int(input())
bacs = []
for i in range(0, nbBacs):
    v = list(map(int, input().split()))
    bacs.append((v[1], v[0]))

bacs.sort()

for s in bacs:
    print(s[1], s[0])
