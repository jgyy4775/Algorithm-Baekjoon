n=int(input())
rope=[]
for _ in range(n):
    rope.append(int(input()))
maxw=0
rope.sort()
for i in range(n):
    sum_weight = rope[i]*(len(rope)-i)
    maxw = max(maxw, sum_weight)
print(maxw)
