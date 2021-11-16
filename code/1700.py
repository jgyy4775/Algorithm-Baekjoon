n, k = map(int, input().split())
product = list(map(int, input().split()))

hole = []
cnt = 0
for i in range(0, k):
    if product[i] in hole:
        continue
    if len(hole) < n:
        if product[i] not in hole:
            hole.append(product[i])
    else:
        idxs = []
        for j in range(n):
            try:
                idx = product[i:].index(hole[j])
            except:
                idx = 101
            idxs.append(idx)
        out = idxs.index(max(idxs));print(idxs)
        del hole[out]
        hole.append(product[i])
        cnt+=1
print(cnt)
