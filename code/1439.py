s = input()
cnt = {'0':0, '1':0}
if len(s)>1:
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            cnt[s[i]] += 1
    cnt[s[i+1]] += 1  ## 010101
print(min(list(cnt.values())))
