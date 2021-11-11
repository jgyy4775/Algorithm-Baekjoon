from collections import deque
m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    xmin, ymin, xmax, ymax = map(int, input().split())
    w, h = xmax - xmin, ymax - ymin
    for i in range(ymin, ymax):
        for j in range(xmin, xmax):
            graph[i][j] = 1
def bfs(i, j):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((i, j))
    cnt=1
    while queue:
        ii, jj = queue.popleft()
        for c in range(4):
            x = jj + dx[c]
            y = ii + dy[c]
            if 0 <= y < m and 0 <= x < n:
                if graph[y][x] == 0:
                    graph[y][x] = 1
                    queue.append((y, x))
                    cnt+=1
    return cnt
result = []
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            graph[i][j]=1
            res = bfs(i,j)
            result.append(res)

print(len(result))
print(*sorted(result))
