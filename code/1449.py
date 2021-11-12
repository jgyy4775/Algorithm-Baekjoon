n, l = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort(reverse = True)
cnt = 0
start,end = 0,1
while True:
    if start >= n or end >= n:
        cnt += 1
        break
    if pos[start] - pos[end] < l:
        end += 1
    else:
        cnt += 1
        start = end
        end = start +1

print(cnt)
