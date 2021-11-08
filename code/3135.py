import sys
a, b = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
flist = []
sublist = []
for i in range(n):
    flist.append(int(sys.stdin.readline()))

for i in range(n):
    sublist.append(abs(flist[i]-b))
if abs(a-b) > min(sublist):
    result = min(sublist)+1
else:
    result = abs(a-b)
print(result)
