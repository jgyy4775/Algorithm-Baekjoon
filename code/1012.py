import sys
from collections import deque

tnum = int(input())
n = [0]*tnum
m = [0]*tnum
k = [0]*tnum
graphs =[0]*tnum
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graphs, i, j, t):
    queue = deque()
    queue.append((i, j))
    while queue:
        ii, jj = queue.popleft()
        for c in range(4):
            x = ii + dx[c]
            y = jj + dy[c]
            if 0 <= x < n[t] and 0 <= y < m[t]:
                if graphs[x][y] == 1:
                    graphs[x][y] = 0
                    queue.append((x, y))
for t in range(tnum):
    m[t], n[t], k[t] = map(int, sys.stdin.readline().split())
    graphs[t] = [[0]*m[t] for i in range(n[t])]
    for c in range(k[t]):
        a, b = map(int, sys.stdin.readline().split())
        graphs[t][b][a] = 1

for t in range(tnum):
    cnt = 0
    for i in range(n[t]):
        for j in range(m[t]):
            if graphs[t][i][j] == 1:
                bfs(graphs[t], i, j, t)
                cnt+=1
    print(cnt)
