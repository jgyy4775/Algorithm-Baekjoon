import sys
sys.setrecursionlimit(100000)
n = int(input())
graph = []
for _ in range(n):
    graph.append(sys.stdin.readline())

def dfs(i, j):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visit[i][j] = True
    for d in range(4):
        y = i + dy[d]
        x = j + dx[d]
        if 0 <= y < n and 0 <= x < n:
            if graph[y][x] == graph[i][j] and visit[y][x] == False:
                dfs(y, x)

visit = [[False] * n for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            dfs(i, j)
            cnt += 1
print(cnt, end = ' ')

graph = [g.replace('R','G') for g in graph]
visit = [[False] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            dfs(i, j)
            cnt += 1
print(cnt)
