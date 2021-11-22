t, w = map(int, input().split())
tree = [0]
dp = [[0]*(w+1) for _ in range(t+1)]
for _ in range(t):
    tree.append(int(input()))
for i in range(1, t+1):
    if tree[i] == 1: # 한번도 안움직일때 => 1번 나무 밑에 있을 때만 먹을 수 있음
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, w+1): # 이동 횟수를 계속 체크
        if j > i:
            break
        if tree[i] == 1 and j % 2 == 0: # 자두가 1번 나무에서 떨어지고 그걸 먹는 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) +1
        elif tree[i] == 2 and j%2 ==1: # 자두가 2번 나무에서 떨어지고 그걸 먹는 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) +1
        else: # 그 외의 경우(안 먹는 경우)
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[-1]))
