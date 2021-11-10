n, k = map(int, input().split())
wvlist = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    wvlist.append((w, v))

dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1,k+1):
        w = wvlist[i][0]
        v = wvlist[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
print(dp[n][k])