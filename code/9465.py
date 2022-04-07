import sys
tc=int(input())
for _ in range(tc):
    n=int(input())
    score,dp = [], [[0]*n for _ in range(2)]
    for i in range(2):
        score.append(list(map(int, sys.stdin.readline().split())))
    for j in range(1, n):
        if j==1:
            score[0][j]+=score[1][j-1]
            score[1][j]+=score[0][j-1]
        else:
            score[0][j]+=max(score[1][j-1], score[1][j-2])
            score[1][j]+=max(score[0][j-1], score[0][j-2])
    print(max(score[0][n-1], score[1][n-1]))
