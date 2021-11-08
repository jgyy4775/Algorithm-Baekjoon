n = int(input())
times = list(map(int, input().split()))
result = 0
times.sort()
for i in range(0, n):
    result += times[i] * (n-i)

print(result)
