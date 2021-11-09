import heapq
import sys
V, E = map(int, sys.stdin.readline().split())
start = int(input())
graph = [[] for i in range(V+1)]
distance = [int(1e9)]*(V+1)
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v,w])
def dijkstra(start):
    q = []
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
dijkstra(start)
for i in distance[1:]:
    if i == int(1e9): print("INF")
    else:
        print(i)
