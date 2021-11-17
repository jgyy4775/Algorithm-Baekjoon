from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j]=='R':  ## 빨간 공 위치 저장
            rx, ry = i, j
        elif graph[i][j]=='B': ## 파란 공 위치 저장
            bx, by = i, j
def bfs(rx, ry, bx, by):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((rx,ry, bx,by))
    visit = []
    visit.append((rx, ry, bx, by))
    count = 0
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if count > 10:
                print(-1)
                return
            if graph[rx][ry] == 'O':
                print(count)
                return
            for i in range(4):  ## 현재 위치에서 동서남북 탐색
                drx, dry = rx, ry
                while True:  ## 벽이나 구멍을 만날때까지 빨간공을 한방향으로 진행
                    drx += dx[i]
                    dry += dy[i]
                    if graph[drx][dry] == '#': # 벽을 만나면 한칸 이전으로 이동
                        drx -= dx[i]
                        dry -= dy[i]
                        break
                    if graph[drx][dry] == 'O':
                        break
                dbx, dby = bx, by
                while True:  ## 벽이나 구멍을 만날때까지 파란공을 한방향으로 진행
                    dbx += dx[i]
                    dby += dy[i]
                    if graph[dbx][dby] == '#': # 벽을 만나면 한칸 이전으로 이동
                        dbx -= dx[i]
                        dby -= dy[i]
                        break
                    if graph[dbx][dby] == 'O':
                        break
                if graph[dbx][dby] == 'O': # 파란 구슬이 먼저 구멍에 들어가는 경우
                    continue
                if drx == dbx and dry == dby: # 두 구슬의 위치가 같고
                    if abs(drx-rx) + abs(dry-ry) > abs(dbx-bx)+abs(dby-by): # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                        drx -= dx[i]
                        dry -= dy[i]
                    else:
                        dbx -= dx[i]
                        dby -= dy[i]
                if (drx, dry, dbx, dby) not in visit: # 방문한적 없는 위치면 큐에 추가 후 방문 처리
                    q.append((drx, dry, dbx, dby))
                    visit.append((drx, dry, dbx, dby))
        count += 1
    print(-1)
bfs(rx, ry, bx, by)
