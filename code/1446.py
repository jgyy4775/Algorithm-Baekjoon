import sys
n, d = map(int, sys.stdin.readline().split())
info=[]
for _ in range(n):
    info.append(list(map(int,sys.stdin.readline().split())))
dp=[i for i in range(d+1)]
info.sort()
for r in info:
    if r[1]>d: continue
    for i in range(d+1):
        if i==r[1]: dp[i]=min(dp[i], dp[r[0]]+r[2])
        elif r[1]<i: dp[i]=min(dp[i],dp[r[1]]+(i-r[1]))
print(dp[-1])
