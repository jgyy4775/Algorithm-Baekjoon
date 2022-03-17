n=int(input())
num=int(input())
mat = [[0]*n for _ in range(n)]
now, start, end = n*n, 0, n-1
while True:
    if start-end == 0:
        mat[start][end]=1
        break
    for i in range(start, end):
        mat[i][start]=now
        now-=1
    for i in range(start, end):
        mat[end][i]=now
        now-=1
    for i in range(end,start,-1):
        mat[i][end]=now
        now-=1
    for i in range(end,start,-1):
        mat[start][i]=now
        now-=1
    end, start = end-1, start+1
for i in range(n):
    print(' '.join(str(ii) for ii in mat[i]))
    for j in range(n):
        if mat[i][j]==num: x,y=i,j
print(x+1,y+1)
