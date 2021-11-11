from collections import deque

def bfs(i, j,m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((i, j))
    while queue:
        ii, jj = queue.popleft()
        for c in range(4):
            x = ii + dx[c]
            y = jj + dy[c]
            if 0 <= x < n and 0 <= y < n:
                if ttmp[x][y] > m:
                    ttmp[x][y] = 0
                    queue.append((x, y))

n = int(input())
maxm = 0
graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    if maxm < max(tmp):
        maxm = max(tmp)
    graph.append(tmp)
maxc = 0
import copy
for m in range(0, maxm+1):
    ttmp = copy.deepcopy(graph)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ttmp[i][j] > m:
                ttmp[i][j] = 0
                bfs(i,j,m)
                cnt += 1
    if maxc < cnt:
        maxc = cnt

print(maxc)
