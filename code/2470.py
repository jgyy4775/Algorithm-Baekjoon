n = int(input())
nlist = list(map(int, sys.stdin.readline().split()))
nlist.sort()
left, right = 0, n-1
ll, rr = left, right
now = nlist[left] + nlist[right]
while left < right:
    tmp = nlist[left] + nlist[right]
    if abs(tmp) < abs(now):
        now = tmp
        ll = left
        rr = right
        if now == 0:
            break
    if tmp < 0:
        left += 1
    elif tmp > 0:
        right -= 1
print(nlist[ll], nlist[rr])
