import sys
str = sys.stdin.readline()
str=str.strip()
answer, tmp, i = [], '', 0
while i<len(str):
    if str[i]=='<':
        if tmp: answer.append(tmp[::-1])
        tmp=''
        for j in range(i, len(str)):
            tmp+=str[j]
            if str[j]=='>':break
        answer.append(tmp)
        i+=len(tmp)-1
        tmp=''
    elif str[i]==' ':
        answer.append(tmp[::-1]+' ')
        tmp=''
    else: tmp+=str[i];
    i+=1
if tmp:answer.append(tmp[::-1])
print(''.join(answer))
