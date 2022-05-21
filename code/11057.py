n=int(input())
dp=[[0]*10 for _ in range(n+1)]
dp[1]=[1 for _ in range(10)]
for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j]+=dp[i-1][k]
print(sum(dp[-1])%10007)
