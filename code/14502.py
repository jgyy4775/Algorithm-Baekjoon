import sys
import copy
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []
dx=[-1,1,0,0]
dy=[0,0,-1,1]
answer=0
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def wall(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                wall(cnt+1)
                graph[i][j]=0

def bfs():
    q=deque()
    tmp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2: q.append([i,j])
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny]==0:
                tmp[nx][ny]=2
                q.append([nx,ny])
    cnt=0
    global answer
    for i in range(n):
        cnt+=tmp[i].count(0)
    answer=max(answer, cnt)
wall(0)
print(answer)
