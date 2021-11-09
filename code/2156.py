n = int(input())
glist = []
for i in range(n):
    glist.append(int(input()))
d = [0] * (n+1)
d[1] = glist[0]
if n>1:
    d[2] = glist[0] + glist[1]
for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-2]+glist[i-1], d[i-3]+glist[i-2]+glist[i-1])
print(d[n])
