n = int(input())
if n==1 or n==3:
    print(-1)
    exit()
elif (n%5)%2 == 0:
    result = n//5 + (n%5)//2
else:
    result = (n//5)-1 + (n%5+5)//2
print(result)
