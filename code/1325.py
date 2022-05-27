import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
res, answer = 0, []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

def bfs(graph, start, visit):
    queue = deque([start])
    ans=0
    visit[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                ans+=1
                visit[i] = True
    return ans

for i in range(1, n+1):
    visit=[False]*(n+1)
    ans = bfs(graph, i, visit)
    if ans>res: res=ans
    answer.append([i, ans])
for i, a in answer:
    if a==res: print(i, end=' ')
