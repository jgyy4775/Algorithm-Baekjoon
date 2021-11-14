import math
tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    res = math.factorial(m)//(math.factorial(n)*math.factorial(m-n))
    print(res)
