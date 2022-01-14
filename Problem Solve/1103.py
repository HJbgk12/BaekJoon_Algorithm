import sys
sys.setrecursionlimit(10**6)


def dfs(y,x):
    global cnt,mx, state

    if y < 0 or x < 0 or y >= n or x >= m:
        return 0
    if visited[y][x]:
        state = True
        return -1
    if mem[y][x] != -1:
        return mem[y][x]
    if g[y][x] == 'H':
        return 0
    visited[y][x] = True
    for i in range(4):
        mem[y][x] = max(mem[y][x], dfs(y + dy[i]* int(g[y][x]), x + dx[i]*int(g[y][x]))+1)
        # ny, nx = y + int(g[y][x]) * dy[i], x + int(g[y][x]) * dx[i]
        if state:
            return -1
    visited[y][x] = False
    return mem[y][x]


n,m = map(int, input().split())

g = []
for i in range(n):
    x = sys.stdin.readline().strip()
    g.append(list(x))
h = []
visited = [[False for _ in range(m)]for _ in range(n)]
mem = [[-1 for _ in range(m)]for _ in range(n)]
state = False
dy = [-1,0,1,0]
dx = [0,-1,0,1]
cnt = 0
mx = 0
print(dfs(0,0))
