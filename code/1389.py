## 너비우선탐색 이용
import sys
from collections import deque
n, m = map(int, input().split())
friend = [[]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    friend[a].append(b)
    friend[b].append(a)
cb=[]
for i in range(1, n+1):
    cnt=0
    for j in range(1, n+1):
        if i==j: continue
        visited = [False] * (n+1)
        visited[i] = True
        q=deque([])
        q.append([i,0])
        while q:
            a,c=q.popleft()
            visited[a]=True
            if a==j:
                cnt+=c
                break
            for g in friend[a]:
                if not visited[g]:
                    q.append([g,c+1])
                    visited[g]=True
    cb.append(cnt)
print(cb.index(min(cb))+1)
import sys
n, m = map(int, input().split())
friend = [[int(1e9)]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    friend[a][b]=1
    friend[b][a]=1
for a in range(1, n + 1):
    friend[a][a] = 0
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            friend[a][b] = min(friend[a][b], friend[a][k] + friend[k][b])
minum=int(1e9)
for i in range(1, n+1):
    tmp=sum(friend[i][1:])
    if minum>tmp:
        answer=i
        minum=tmp
print(answer)

## 플로이드 워셜 이용
