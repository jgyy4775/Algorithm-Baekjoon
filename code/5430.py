import sys
from collections import deque
tc=int(sys.stdin.readline())
for _ in range(tc):
    p=sys.stdin.readline().strip()
    n=int(sys.stdin.readline())
    x=sys.stdin.readline().strip()
    r=0
    if x=='[]':x=[]
    else: x=list(x[1:-1].split(','))
    x=deque(x)
    for s in p:
        if s=='R': r+=1
        else:
            if len(x)==0: print('error'); break
            if r%2==0: x.popleft()
            else: x.pop()
    else:
        if r%2==1: print('[' + ','.join(list(reversed(x)))+ ']')
        else: print('[' + ','.join(list(x))+ ']')
