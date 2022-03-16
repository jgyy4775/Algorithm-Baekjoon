n=int(input())
a,b=0,0
for i in range(1, n+1):
    if i%2==0:
        while i%2==0:
            a+=1
            i/=2
    if i%5==0:
        while i%5==0:
            b+=1
            i/=5
print(min(a,b))

'''
n=int(input())
cnt=0
while n>=5:
    cnt+=n//5
    n//=5
print(cnt)
'''
