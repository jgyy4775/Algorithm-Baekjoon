import sys
from itertools import permutations
n=int(input())
nlist=list(map(int, sys.stdin.readline().split()))
nlist = list(permutations(nlist, n))
answer=0
for nn in nlist:
    tmp=0
    for i in range(n-1):
        tmp+=abs(nn[i]-nn[i+1])
    answer=max(answer,tmp)
print(answer)
