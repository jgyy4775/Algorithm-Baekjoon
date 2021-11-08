import sys
n= int(input())
nlist = sorted(list(map(int, sys.stdin.readline().split())))
m = int(input())
mlist = list(map(int, sys.stdin.readline().split()))

for i in range(len(mlist)):
    flag = 0
    start = 0
    end = len(nlist)-1
    while start <= end:
        mid = (start+end)//2
        if nlist[mid] == mlist[i]:
            print(1)
            flag = 1
            break
        elif nlist[mid] > mlist[i]:
            end = mid-1
        else:
            start = mid+1
    if flag == 0:
        print(0)
