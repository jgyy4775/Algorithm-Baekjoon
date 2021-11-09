n = int(input())
nlist = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if nlist[i] > nlist[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
