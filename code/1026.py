import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
atmp = sorted(a)
btmp = sorted(b, reverse = True)
sum=0
for i in range(n):
    sum += atmp[i] * btmp[i]
print(sum)
