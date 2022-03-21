s=input()
stack = []
for ch in s:
    if ch == ')':
        if len(stack) == 0: print(0);exit()
        tmp,fin=0,1;
        while len(stack)!=0:
            c=stack.pop()
            if c=='(':
                stack.append(fin*2)
                break
            elif type(c)==int:
                tmp+=c
                fin=tmp
            else:
                print(0)
                exit()
    elif ch == ']':
        if len(stack)==0:print(0);exit()
        tmp,fin = 0,1;
        while len(stack) != 0:
            c = stack.pop()
            if c == '[':
                stack.append(fin*3)
                break
            elif type(c)==int:
                tmp+=c
                fin=tmp
            else:
                print(0)
                exit()
    else: stack.append(ch)

print(0 if "(" in stack or "[" in stack or ")" in stack or "]" in stack else sum(stack))
