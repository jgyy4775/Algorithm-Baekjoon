import sys
n, m = map(int, input().split())
dulist = []
nlist = list(map(int, sys.stdin.readline().split()))
nlist.insert(0,0)
for _ in range(m):
    dulist.append(list(map(int, sys.stdin.readline().split())))
for i in range(1,n+1):
    nlist[i]=nlist[i-1]+nlist[i]
for du in dulist:
    print(nlist[du[1]]-nlist[du[0]-1])
