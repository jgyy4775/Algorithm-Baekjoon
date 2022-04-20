import sys
n = int(sys.stdin.readline())
height= list(map(int, sys.stdin.readline().split()))
answer,stack=[],[]
for i in range(n):
    while stack:
        if stack[-1][1]>height[i]:
            answer.append(stack[-1][0]+1)
            break
        else: stack.pop()
    if not stack: answer.append(0)
    stack.append([i, height[i]])
print(' '.join(map(str, answer)))
