import sys
import heapq
n = int(sys.stdin.readline())
card=[]
for _ in range(n):
    card.append(int(sys.stdin.readline()))
heapq.heapify(card)
answer=0
while len(card)>1:
    tmp1, tmp2 = heapq.heappop(card), heapq.heappop(card)
    answer+=tmp1+tmp2
    heapq.heappush(card, tmp1+tmp2)
print(answer)
