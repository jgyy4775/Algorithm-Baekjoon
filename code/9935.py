import sys
allstr = sys.stdin.readline().strip()
bomb=sys.stdin.readline().strip()
stack=[]
for s in allstr:
    stack.append(s)
    if ''.join(stack[len(stack)-len(bomb):])==bomb:
        for i in range(len(bomb)): stack.pop()
print("FRULA" if len(stack)==0 else ''.join(stack))
