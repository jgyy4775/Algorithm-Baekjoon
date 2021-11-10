from collections import deque
n, m = map(int, input().split())
graph = []
queue = deque()

for i in range(m):
    graph.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i,j))
def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        ii, jj = queue.popleft()
        for c in range(4):
            x = ii + dx[c]
            y = jj + dy[c]
            if 0 <= x < m and 0 <= y < n:
                if graph[x][y] == 0:
                    queue.append((x, y))
                    graph[x][y] = graph[ii][jj] + 1

bfs()
result = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result-1)
