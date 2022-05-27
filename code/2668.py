import sys
n = int(sys.stdin.readline())
graph=[0]
for i in range(n):
    a = int(sys.stdin.readline())
    graph.append(a)
answer=set()
def dfs(first, second, num):
    first.add(num)
    second.add(graph[num])
    if graph[num] in first:
        if first==second:
            answer.update(first)
            return True
        return False
    return dfs(first, second, graph[num])

for i in range(1, n+1):
    if i not in answer: dfs(set(),set(),i)

print(len(answer))
print(*sorted(list(answer)), sep='\n')
