import sys
n, c = map(int, sys.stdin.readline().split())
house=[]
for _ in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()
start, end = 1, house[-1]-house[0]
answer=0
while start<=end:
    mid=(start+end)//2
    cnt=1
    tmp=house[0]
    for i in range(1,n):
        if house[i]-tmp>=mid:
            cnt+=1
            tmp=house[i]
    if cnt>=c:
        answer=mid
        start=mid+1
    else: end=mid-1
print(answer)
