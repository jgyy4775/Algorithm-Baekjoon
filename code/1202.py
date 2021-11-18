import heapq
import sys
n, k = map(int, sys.stdin.readline().split())
jewel = []
bag = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, (m, v))
for _ in range(k):
    bag.append(int(input()))
jewel.sort()
bag.sort()
q =[]
vsum = 0
for b in bag:
    while jewel and b >= jewel[0][0]: # 가방에 담을 수 있는 보석이 있다면 
        w, v = heapq.heappop(jewel) # 그걸 꺼내고
        heapq.heappush(q, -v) # '-'를 붙여 값을 넣어줌(최대힙 q 만드는 방법)
    if q: # 넣을 수 있는 보석이 있다면
        vsum -= heapq.heappop(q) # q에서 그 값을 꺼내어 vsum에 더해주기
    elif not jewel:
        break

print(vsum)
