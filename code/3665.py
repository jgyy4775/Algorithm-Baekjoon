import heapq
import sys
from collections import deque
def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] ==0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in team[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    if len(result) < n:
        print('IMPOSSIBLE', end=' ')
    else:
        for i in result:
            print(i, end=' ')
    print()
tc = int(input())
for _ in range(tc):
    n = int(input())
    lastgrade = list(map(int, sys.stdin.readline().split()))
    team = [[] for i in range(n + 1)]
    indegree = [0] * (n + 1)  # 진입차수

    for i in range(n-1):
        for j in range(i+1, n):
            team[lastgrade[i]].append(lastgrade[j])
            indegree[lastgrade[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        check = True
        for i in team[a]:
            if i == b:
                team[a].remove(b)
                team[b].append(a)
                indegree[b] -= 1
                indegree[a] += 1
                check = False
        if check:
            team[b].remove(a)
            team[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
    topology_sort()
