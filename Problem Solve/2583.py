import sys
sys.setrecursionlimit(10**6)
def dfs(y,x):
    visited[y][x] = 1
    global tot
    for i in range(4):
        ny,nx = y + dy[i], x + dx[i]
        if 0 <= ny < m and 0 <= nx < n:
            if g[y][x] == g[ny][nx] and not visited[ny][nx]:
                dfs(ny, nx)
    tot += 1

m,n,k = map(int,input().split())

g = [[0 for _ in range(n)] for _ in range(m)]

for i in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            g[y][x] = 1

visited = [[0 for _ in range(n)] for _ in range(m)]

cnt = 0
dx = [0,1,0,-1]
dy = [-1,0,1,0]
res = []
for y in range(m):
    for x in range(n):
        if not visited[y][x] and g[y][x] == 0:
            tot = 0
            dfs(y,x)
            cnt += 1
            res.append(tot)

print(cnt)
res.sort()
for x in res:
    print(x, end = " ")





