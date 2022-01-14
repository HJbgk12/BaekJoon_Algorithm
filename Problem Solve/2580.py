import sys

def check(b, a):
    y, x = (b[0] // 3) * 3, (b[1] // 3) * 3
    temp = []
    for i in range(y,y+3):
        for j in range(x,x+3):
            temp += [g[i][j]]
    if not a in g[b[0]] and not a in [i[b[1]] for i in g] and not a in temp:
        return 1
    return 0

def dfs(b):
    if b == len(key):
        for y in range(9):
            for x in range(9):
                print(g[y][x],end = ' ')
            print()
        sys.exit()
    else:
        if blank[key[b]]:
            for a in blank[key[b]]:

                if check(key[b], a):
                    g[key[b][0]][key[b][1]] = a
                    dfs(b+1)
                    g[key[b][0]][key[b][1]] = 0
        else:
            dfs(b+1)


g = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

blank = {}
for y in range(9):
    for x in range(9):
        if g[y][x] == 0:
            blank[y,x] = []

c = set([i for i in range(1,10)])
for b in blank.keys():
    temp1 = set(g[b[0]]) # 가로줄
    temp2 = set([i[b[1]] for i in g])# 세로줄
    temp3 = []
    y, x  = (b[0] // 3)*3, (b[1] // 3)*3
    for i in range(y,y+3):
        for j in range(x,x+3):
            temp3 += [g[i][j]]
    temp = list(c - temp1.union(temp2.union(set(temp3))))
    for t in temp:
        blank[b].append(t)

for b in blank:
    if len(blank[b]) == 1:
        g[b[0]][b[1]] = blank[b][0]
        blank[b] = []
key = list(blank.keys())
dfs(0)

