n= int(input())
nlist = []
for _ in range(n):
    nlist.append(float(input()))
dp = [0]*n
dp[0] = nlist[0]
for i in range(1, n):
    dp[i] = max(nlist[i], nlist[i] * dp[i-1])
print("%.3f" %(max(dp)))
