import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
if n==k:print(0);exit()
visit=[False]*100001
q=deque()
q.append([n,0])
while q:
    x,a=q.popleft()
    if x+1==k: print(a+1);break
    else:
        if 0<=x+1<100001 and not visit[x+1]:
            q.append([x+1, a+1])
            visit[x+1]=True

    if x-1==k: print(a+1);break
    else:
        if 0<=x-1<100001 and not visit[x-1]:
            q.append([x-1, a+1])
            visit[x-1]=True

    if 2*x==k: print(a+1);break
    else:
        if 0<=2*x<100001 and not visit[2*x]:
            q.append([2*x, a+1])
            visit[2*x]=True
