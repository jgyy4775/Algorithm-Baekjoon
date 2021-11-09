def bellman_ford(start):
    distance[start] = 0
    for _ in range(n-1):
        for j in range(1, n+1):
            for v,c in graph[j]:
                if distance[v] > distance[j] + c:
                    distance[v] = distance[j] + c
    for j in range(1, n+1):
        for v, c in graph[j]:
            if distance[v] > distance[j] +c:
                return False
    return distance

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [float('inf')] * (n+1)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

distance = bellman_ford(1)
if distance == False:
    print(-1)
else:
    for i in range(2, n+1):
        print(distance[i] if distance[i] < float('inf') else -1)
