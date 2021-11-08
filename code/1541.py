sublist = input().split('-')
plusres = []
for s in sublist:
    pluslist = s.split('+')
    sumn = 0
    for p in pluslist:
        sumn += int(p)
    plusres.append(sumn)

for i, p in enumerate(plusres):
    if i == 0:
        n = p
    else:
        n -= p
print(n)
