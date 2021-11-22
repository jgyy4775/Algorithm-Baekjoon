n = int(input())
univ = []
for _ in range(n):
    p, d = map(int, input().split())
    univ.append((d, p))

univ.sort()
lec = []
for i in range(n):
    heapq.heappush(lec, univ[i][1])
    if univ[i][0] < len(lec):
        heapq.heappop(lec)
print(sum(lec))
