from random import randint
from time import time

n = 10
# l = list(map(int, input().split()))
L = [randint(0, 300000) for i in range(1, 20001)]
x = [randint(0, 300000) for i in range(1, 20001)]
a = time()
d = 20000

L.sort()


def search(Li, q):
    length = len(Li)
    # print(length)
    # print(Li)
    if length == 1:
        if q == Li[0]:
            return 1
        else:
            return 0
    else:
        if q <= Li[length // 2 - 1]:
            return search(Li[0:length // 2], q)
        else:
            return search(Li[length // 2:length], q)


for i in range(0, d):
    q = x[i]
    print(search(L, q))


print(time() - a)
