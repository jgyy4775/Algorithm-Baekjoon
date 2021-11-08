import sys
n = int(input())
graph = [[0]*n for _ in range(n)]

for i in range(n):
    tmp = sys.stdin.readline()
    for j in range(n):
        if int(tmp[j]) == 1:
            graph[i][int(j)] = 1
visit = [[False]*n for _ in range(n)]
def dfs(i, j, num):
    visit[i][j] = True
    num += 1
    for d in range(4):
        y = i + dy[d]
        x = j + dx[d]
        if 0 <= y <n and 0 <= x < n:
            if graph[y][x] == 1 and visit[y][x] == False:
                num = dfs(y,x,num)
    return num
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = []
dange = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visit[i][j]:
            result.append(dfs(i,j,0))
            dange += 1
result.sort()
print(dange)
for r in result:
    print(r)
