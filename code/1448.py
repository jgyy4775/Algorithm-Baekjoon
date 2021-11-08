import sys
n = int(input())
tlist = []
for i in range(n):
    tlist.append(int(sys.stdin.readline()))
tlist.sort(reverse=True)
result =0
for i in range(n-2):
    if tlist[i+1]+tlist[i+2] > tlist[i]:
        result= tlist[i+1]+tlist[i+2] + tlist[i]
        break
if result ==0:
    result = -1
print(result)
