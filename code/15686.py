import sys
from itertools import combinations
n,m=map(int, sys.stdin.readline().split())
city,house,chic = [],[],[]
for i in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if city[-1][j]==1: house.append([i,j])
        if city[-1][j]==2: chic.append([i,j])
combi=list(combinations(chic, m))
answer=10000
for com in combi:
    dsum=0
    for h in house:
        tmp=10000
        for c in com:
            tmp=min(tmp, abs(h[0]-c[0])+abs(h[1]-c[1]))
        dsum+=tmp
    answer=min(dsum, answer)
print(answer)
