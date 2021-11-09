from collections import deque
n, m = map(int, input().split())
student = [[] for i in range(n+1)]
indegree = [0] * (n+1) # 진입차수
for _ in range(m):
    a, b = map(int, input().split())
    student[a].append(b)
    indegree[b] += 1
def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] ==0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in student[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')
topology_sort()
