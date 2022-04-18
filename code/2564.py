import sys

m,n = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
store=[]
for _ in range(c):
    store.append(list(map(int, sys.stdin.readline().split())))
d,x=map(int, sys.stdin.readline().split())
answer=0
for s in store:
    if s[0]==d: answer+=abs(x-s[1])
    else:
        if d==1:
            if s[0]==2: answer+=min(s[1]+n+x, m-s[1]+n+m-x)
            elif s[0]==3: answer+=s[1]+x
            elif s[0]==4: answer+=m-x+s[1]
        if d==2:
            if s[0]==1: answer+=min(s[1]+n+x, m-s[1]+n+m-x)
            elif s[0]==3: answer+=n-s[1]+x
            elif s[0]==4: answer+=m-x+n-s[1]
        if d==3:
            if s[0]==2: answer+=n-x+s[1]
            elif s[0]==1: answer+=s[1]+x
            elif s[0]==4: answer+=min(x+m+s[1], n-x+m+n-s[1])
        if d==4:
            if s[0]==2: answer+=m-s[1]+n-x
            elif s[0]==3: answer+=min(x+m+s[1], n-x+m+n-s[1])
            elif s[0]==1: answer+=m-s[1]+x
print(answer)
