a = input()
b = input()
alpha = {'A':3, 'B':2, 'C':1, 'D':2, 'E':3, 'F':3, 'G':2, 'H':3, 'I':3,
         'J':2, 'K':2, 'L':1, 'M':2, 'N':2, 'O':1, 'P':2, 'Q':2, 'R':2,
         'S':1, 'T':2, 'U':1, 'V':1, 'W':1, 'X':2, 'Y':2, 'Z':1 }
for k, v in alpha.items():
    a = a.replace(k,str(v))
    b = b.replace(k,str(v))
tmp = []
for aa, bb in zip(a,b):
    tmp.append(int(aa))
    tmp.append(int(bb))

while len(tmp)>2:
    ttmp = []
    for i in range(1, len(tmp)):
        ttmp.append((tmp[i-1] + tmp[i])%10)
    tmp = ttmp
result = ''
for i in tmp:
    result+=str(i)
print(result)
