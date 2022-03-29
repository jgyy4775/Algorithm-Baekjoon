import sys
n = int(input())
price=[]
for _ in range(n):
    price.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n):
    for j in range(3):
        price[i][j]+=min(price[i-1][:j]+price[i-1][j+1:])
print(min(price[-1]))
