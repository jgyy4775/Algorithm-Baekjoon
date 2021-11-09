n = int(input())
roadlist = list(map(int, input().split()))
oillist = list(map(int, input().split()))
sum = 0
minimum = oillist[0]
for i in range(n-1):
    if minimum > oillist[i]:
        minimum = oillist[i]
    sum += (minimum*roadlist[i])
print(sum)
