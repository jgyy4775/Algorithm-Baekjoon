n, m = map(int, input().split())
lecmin = list(map(int, input().split()))

start = sum(lecmin)//m
end = sum(lecmin)
res = end
while start <= end:
    mid = (start+end)//2
    if mid < max(lecmin):
        start = mid + 1
        continue
    cnt, tmp = 0, 0
    for i in range(n):
        if lecmin[i] > mid:
            break
        elif tmp + lecmin[i] <= mid:
            tmp += lecmin[i]
        else:
            tmp = lecmin[i]
            cnt += 1
    if cnt <= m-1:
        end = mid-1
        res=min(res, mid)
    else:
        start=mid+1
print(res)
