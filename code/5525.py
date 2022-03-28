import sys
n=int(input())
m=int(input())
str = sys.stdin.readline()
pat, answer, i = 0, 0 ,1
while i<m-1:
    if str[i-1]=='I' and str[i]=='O' and str[i+1]=='I':
        pat+=1
        if pat==n:
            pat-=1
            answer+=1
        i+=1
    else: pat=0
    i+=1
print(answer)
