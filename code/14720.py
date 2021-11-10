n = int(input())
store = list(map(int, sys.stdin.readline().split()))
rule = {0: 1, 1:2, 2:0}
now = 0
start = False
cnt=0
for s in store:
    if s == 0 and start == False:
        start = True
        cnt+=1
    if s == rule[now] and start == True:
        cnt += 1
        now = rule[now]
print(cnt)
