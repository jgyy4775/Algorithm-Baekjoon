import sys
n = int(input())
nlist = list(map(int, sys.stdin.readline().split()))

dpi = [1] * n
dpd = [1] * n
for i in range( n):
    for j in range(0, i):
        if nlist[i] > nlist[j]:
            dpi[i] = max(dpi[i], dpi[j] + 1)
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if nlist[i] > nlist[j]:
            dpd[i] = max(dpd[i], dpd[j] + 1)
max = 0
for i in range(n):
    if dpi[i] +dpd[i] > max:
        max = dpi[i] +dpd[i]
print(max-1)
