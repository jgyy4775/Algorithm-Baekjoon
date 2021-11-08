import sys
k, n = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(tree)
result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for t in tree:
        if t > mid:
            total+=(t-mid)
        if total > n:
            break
    if total < n:
        end = mid-1
    else:
        start=mid+1
        result=mid
print(result)
