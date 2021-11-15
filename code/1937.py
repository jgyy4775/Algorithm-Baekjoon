import sys
sys.setrecursionlimit(1000000)

n = int(input())
forest = []
for _ in range(n):
    forest.append(list(map(int,sys.stdin.readline().split())))
visit = [[0] * n for _ in range(n)]
def dfs(i, j):
    if visit[i][j]: return visit[i][j]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    visit[i][j] = 1
    for d in range(4):
        x = i + dx[d]
        y = j + dy[d]
        if 0 <= y < n and 0 <= x < n:
            if forest[x][y] > forest[i][j] :
                visit[i][j] = max(visit[i][j], dfs(x, y)+1)
    return visit[i][j]
