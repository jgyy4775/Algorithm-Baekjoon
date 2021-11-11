n = int(input())
tplist = []
for _ in range(n):
    t, p = map(int, input().split())
    tplist.append((t, p))

dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if tplist[i][0] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], tplist[i][1] + dp[i+tplist[i][0]])
print(dp[0])
