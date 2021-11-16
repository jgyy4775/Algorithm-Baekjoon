import sys
n = int(input())
weight = list(map(int, sys.stdin.readline().split()))
able = []
weight.sort()
res = 1
for i in range(n):
    if res >= weight[i]:
        res += weight[i]
    else:
        break
print(res)
