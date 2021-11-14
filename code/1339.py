n = int(input())
word = []
worddict = {}
for _ in range(n):
    word.append(input())

for w in word:
    square = len(w)-1
    for c in w:
        if c in worddict:
            worddict[c] += pow(10, square)
        else:
            worddict[c] = pow(10, square)
        square -= 1
reslist = sorted(list(worddict.values()), reverse=True)
result, start = 0, 9
for r in reslist:
    result += r*start
    start -= 1
print(result)
