import sys
from collections import deque

def bfs():
    q=deque()
    q.append([0,0,0])
    dx, dy = [1,-1,0,0], [0,0,-1,1]
    visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visit[0][0][0]=1

    while q:
        x,y,c = q.popleft()
        if x==n-1 and y==m-1: return visit[x][y][c]
        for d in range(4):
            xx, yy = x+dx[d], y+dy[d]
            if 0<=xx<n and 0<=yy<m and c==0 and graph[xx][yy]==1:
                q.append([xx,yy,1])
                visit[xx][yy][1]=visit[x][y][0]+1
            elif 0<=xx<n and 0<=yy<m and visit[xx][yy][c]==0 and graph[xx][yy]==0:
                q.append([xx, yy, c])
                visit[xx][yy][c] = visit[x][y][c] + 1
    return -1

n,m=map(int, sys.stdin.readline().split())
graph, wall = [],[]
for i in range(n):
    graph.append(list(map(int,list(sys.stdin.readline().strip()))))

print(bfs())

'''
import sys
from collections import deque

def bfs(graph):
    q=deque()
    q.append([0,0,1])
    dx, dy = [1,-1,0,0], [0,0,-1,1]
    visit = [[False]*m for _ in range(n)]
    visit[0][0]=True
    while q:
        x,y,c = q.popleft()
        if x==n-1 and y==m-1: return c
        for d in range(4):
            xx, yy = x+dx[d], y+dy[d]
            if 0<=xx<n and 0<=yy<m and not visit[xx][yy] and graph[xx][yy]==0:
                q.append([xx,yy,c+1])
                visit[xx][yy]=True
    return int(1e9)

n,m=map(int, sys.stdin.readline().split())
graph, wall = [],[]
for i in range(n):
    tmp=list(map(int,list(sys.stdin.readline().strip())))
    graph.append(tmp)
    for j in range(m):
        if tmp[j]==1: wall.append([i,j])
answer=int(1e9)
for w in wall:
    graph[w[0]][w[1]]=0
    answer=min(bfs(graph), answer)
    graph[w[0]][w[1]]=1
print(-1 if answer==int(1e9) else answer)
'''
