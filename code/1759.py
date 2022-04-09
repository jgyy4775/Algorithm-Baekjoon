import sys
from itertools import combinations
l,c =map(int, sys.stdin.readline().split())
alpha=list(sys.stdin.readline().split())
alpha.sort()
aeiou, bc, answer = [],[],[]
for a in alpha:
    if a=='a' or a=='e' or a=='i' or a=='o' or a=='u': aeiou.append(a)
    else: bc.append(a)
for i in range(1,l):
    ae=list(combinations(aeiou,i))
    if l-i<2:continue
    bcd=list(combinations(bc, l-i))
    for a in ae:
        for b in bcd:
            answer.append(''.join(sorted(a+b)))
answer=sorted(answer)
for a in answer:print(a)
