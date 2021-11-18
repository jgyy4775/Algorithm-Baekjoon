from collections import deque
import sys
def bfs(i):
    q = deque()
    q.append(i)
    visit[i] = 1
    isTrue = True
    while q:
        ii = q.popleft()
        for j in edges[ii]:
            if visit[j] == 0:
                q.append(j)
                visit[j] = -1 * visit[ii]
            elif visit[ii] == visit[j]:
                isTrue = False
    return isTrue

tc = int(input())
for _ in range(tc):
    v, e = map(int, sys.stdin.readline().split())
    edges = [[] for i in range(v+1)]
    visit = [0] * (v+1)
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)

    for i in range(1, v+1):
        if visit[i] == 0:
            flag = bfs(i)
            if flag == False:
                break
    if flag == True:print('YES')
    else:print('NO')
