n = int(input())
res = []
start = 666
while True:
    if len(res) == n:
        break
    if '666' in str(start):
        res.append(start)
    start+=1

print(res[-1])
