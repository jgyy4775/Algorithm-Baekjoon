import heapq

case = int(input())
def dijkstra(start):
    q = []
    distance = [float('inf')]*(n+1)
    time = [float('inf')] * (n+1)
    distance[start] = 0
    time[start] = 0
    heapq.heappush(q, [0, 0, start])
    while q:
        dist, stime, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            sstime = stime + i[2]
            if sstime < time[i[0]]:
                time[i[0]] = sstime
                distance[i[0]] = cost
                heapq.heappush(q, [cost, sstime, i[0]])
    return distance, time

for i in range(case):
    n, m, k = map(int, input().split())
    graph = [[]*(n+1) for _ in range(n+1)]
    for j in range(k):
        u, v, c, d = map(int, input().split())
        graph[u].append([v, c, d])

    distance, time = dijkstra(1)
    if distance[n] > m:
        print("Poor KCM")
    else:
        print(time[n])
