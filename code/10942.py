import sys
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
m = int(input())
dp = [[0] *n for _ in range(n)]
for i in range(n):
    for j in range(n-i):
        end = i + j
        if j == end:
            dp[j][end] = 1
        elif nums[j] == nums[end]:
            if j+1 == end:
                dp[j][end] = 1
            elif dp[j+1][end-1] == 1:
                dp[j][end] = 1
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])
