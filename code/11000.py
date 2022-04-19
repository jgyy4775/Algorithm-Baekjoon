import sys
import heapq

a = int(sys.stdin.readline())
time, endtime=[],[]
for _ in range(a):
    time.append(list(map(int, sys.stdin.readline().split())))
time.sort()
heapq.heappush(endtime, time[0][1])
for t in time[1:]:
    if endtime[0]>t[0]: heapq.heappush(endtime, t[1])
    else:
        heapq.heappop(endtime)
        heapq.heappush(endtime, t[1])
print(len(endtime))
