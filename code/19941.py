import sys
n, k = map(int, input().split())
hp = sys.stdin.readline()[:-1]

cnt = 0
for i in range(n):
    if hp[i] == 'P':
        if i+k+1 < n:
            end = i+k+1
        else:
            end = n
        for j in range(i-k,end):
            if j>=0 and hp[j] == 'H':
                cnt += 1
                hp = hp[:j] + 'X' + hp[j+1:]
                break
print(cnt)
