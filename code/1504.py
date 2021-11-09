import heapq
import sys
V, E = map(int, sys.stdin.readline().split())

graph = [[] for i in range(V+1)]

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v,w])
    graph[v].append([u, w])
vertex1, vertex2 = map(int, input().split())

def dijkstra(start):
    q = []
    distance = [int(1e9)]*(V+1)
    distance[start] = 0
    heapq.heappush(q, [0, start])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
    return distance

start_1 = dijkstra(1)
start_v1 = dijkstra(vertex1)
start_v2 = dijkstra(vertex2)

min_distance = min(start_1[vertex1] + start_v1[vertex2] + start_v2[V],
                   start_1[vertex2] + start_v2[vertex1] + start_v1[V])
if min_distance < int(1e9):
    print(min_distance)
else:
    print(-1)
