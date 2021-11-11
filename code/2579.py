n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))
dp = [0] * n
if n > 3:
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2]+score[i])
    print(dp[n-1])
if n==1: print(score[0])
elif n==2: print(score[0] + score[1])
elif n==3: print(max(score[0] + score[2], score[1] + score[2]))
