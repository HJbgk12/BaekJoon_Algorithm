def dfs(v,s):
    global ans
    if v == m:
        d = 0
        for h in house:
            mn = 21570000
            for c in res:
                if mn > abs(h[0]-c[0]) + abs(h[1]-c[1]):
                    mn = abs(h[0]-c[0]) + abs(h[1]-c[1])
            d += mn
        if ans > d:
            ans = d

        return
    else:
        for i in range(s,len(chicken)):
            res.append(chicken[i])
            dfs(v+1, i+1)
            res.pop()
n,m = map(int, input().split())

g = [[_ for _ in map(int, input().split())]for _ in range(n)]

house = []
chicken = []

for y in range(n):
    for x in range(n):
        if g[y][x] == 1:
            house.append([y,x])
        if g[y][x] == 2:
            chicken.append([y,x])
res = []
mn = 0
ans = 21570000
dfs(0,0)
print(ans)