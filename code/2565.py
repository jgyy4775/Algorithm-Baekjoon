import sys
n=int(sys.stdin.readline())
line,dp=[],[1]*(n)
for _ in range(n):
    line.append(list(map(int, sys.stdin.readline().split())))
line.sort()
for i in range(1,n):
    for j in range(i):
        if line[i][1]> line[j][1]: dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))
