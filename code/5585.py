n = int(input())

mlist = [500, 100, 50, 10, 5, 1]
money = 1000 - n
result = 0
for m in mlist:
    result += money//m
    money %= m

print(result)
