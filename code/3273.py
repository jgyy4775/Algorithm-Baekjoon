n = int(input())
nlist = list(map(int, sys.stdin.readline().split()))
nlist.sort()
x = int(input())
cnt = 0
left, right = 0, n-1
while left < right:
    tmp = nlist[left] + nlist[right]
    if tmp == x:
        cnt += 1
    if tmp < x:
        left += 1
        continue
    right -= 1
print(cnt)
