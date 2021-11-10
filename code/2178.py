import sys
from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(i, j):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append((i, j))
    while queue:
        ii, jj = queue.popleft()
        for c in range(4):
            x = ii + dx[c]
            y = jj + dy[c]
            if 0 <= x < n and 0 <= y < m:
                if graph[x][y] == 1:
                    queue.append((x, y))
                    graph[x][y] = graph[ii][jj] + 1
bfs(0, 0)
print(graph[n-1][m-1])
