import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split())))
def bfs():
    visit=[[False]*m for _ in range(n)]
    q=deque()
    q.append((0,0))
    dx, dy=[-1,1,0,0],[0,0,-1,1]
    cnt=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if matrix[nx][ny]==0 and visit[nx][ny]==False:
                    q.append((nx, ny))
                    visit[nx][ny]=True
                elif matrix[nx][ny]==1:
                    matrix[nx][ny]=0
                    cnt+=1
                    visit[nx][ny]=True
    return cnt
result, time=[],0
while True:
    cnt=bfs()
    result.append(cnt)
    if cnt==0: break
    time+=1
print(time)
print(result[-2])
