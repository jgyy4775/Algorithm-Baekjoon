import sys
n, m, r = map(int, sys.stdin.readline().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
for _ in range(r):
    for i in range(min(n,m)//2):
        x, y = i, i
        svalue = matrix[x][y]
        for j in range(i+1, n-i):  ## 좌
            x=j
            pvalue = matrix[x][y]
            matrix[x][y]=svalue
            svalue=pvalue

        for j in range(i+1, m-i):  ## 하
            y=j
            pvalue=matrix[x][y]
            matrix[x][y]=svalue
            svalue=pvalue
        for j in range(i+1, n-i):  ## 우
            x=n-j-1
            pvalue=matrix[x][y]
            matrix[x][y]=svalue
            svalue=pvalue
        for j in range(i+1, m-i):  ## 상
            y=m-j-1
            pvalue=matrix[x][y]
            matrix[x][y]=svalue
            svalue=pvalue

for i in range(n):
    print(' '.join(str(ii) for ii in matrix[i]))
