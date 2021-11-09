import heapq
import sys
case = int(input())
def dijkstra(start):
    q = []
    distance = [int(1e9)] * (n + 1)
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

for _ in range(case):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for i in range(n + 1)]

    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append([v, w])
        graph[v].append([u, w])
    candiv = []
    for i in range(t):
        candiv.append(int(input()))
    start = dijkstra(s)
    start_g = dijkstra(g)
    start_h = dijkstra(h)
    tmp = []
    for i in candiv:
        if start[g]+start_g[h]+start_h[i]==start[i] or\
            start[h] + start_h[g] + start_g[i] == start[i]:
            tmp.append(i)
    tmp.sort()
    for i in tmp:
        print(i, end=' ')
