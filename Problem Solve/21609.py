import sys

# 일반 블록 m가지 색상
# 검은블록 : -1
# 무지개블록 : 0
# |r1-r2| + |c1-c2| = 1을 만족하는 두칸 (r1,c1),(r2,c2)는 인접한 칸
#
# 그룹에는 일반블록 적어도 하나 포함, 검은블록 x, 무지개블록 노상관, 블록 개수는 2개이상

def find_block(y,x,color):
    global cnt
    for i in range(4):
        my, mx = y + dy[i], x + dx[i]
        if 0 <= my < n and 0 <= mx < n and g[my][mx] != -1 and g_map[my][mx] == 0 and g[my][mx] != 'x':
            if g[my][mx] == 0 or g[my][mx] == color:
                g_map[my][mx] = 1
                if g[my][mx] != 0:
                    if standard_block[0] > my:
                        standard_block[0] = my
                    if standard_block[1] > mx:
                        standard_block[1] = mx
                else:
                    check[0] += 1
                cnt += 1
                find_block(my,mx, color)
    return

def gravity(g):
    for i in range(n-2,-1,-1):
        for j in range(n):
            if g[i][j] != -1 and g[i][j] != 'x':
                d = 0
                while g[i+d+1][j] == 'x':
                    d += 1
                    if i+d+1 > n-1:
                        break
                g[i][j], g[i+d][j] = 'x',g[i][j]

def rotate():
    result = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[n-j-1][i] = g[i][j]
    return result

n,m = map(int, input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
g = []
for i in range(n):
    g.append(list(map(int, sys.stdin.readline().split())))

score = 0
temp = [[0 for _ in range(n)] for _ in range(n)]
check_temp = [0,0,0]
# 큰 블록 찾기
xx = 0
s = 0
while True:
    res = 0
    flag = 1
    s += 1
    for y in range(n):
        for x in range(n):
            if g[y][x] == -1 or g[y][x] == 0 or g[y][x] == 'x':
                continue
            else:
                g_map = [[0 for _ in range(n)] for _ in range(n)]
                standard_block = [y,x] # 기준블록
                check = [0,0,0] # 무지개 블록 수, 기준블록 행의 번호, 기준블록 열의 번호
                g_map[y][x] = 1
                cnt = 1
                find_block(y, x, g[y][x])
                check[1], check[2] = standard_block[0], standard_block[1]

                if cnt < 2:
                    continue
                else:
                    flag = 0
                    if res < cnt:
                        res = cnt
                        for i in range(len(check)):
                            check_temp[i] = check[i]
                        for i in range(n):
                            for j in range(n):
                                temp[i][j] = g_map[i][j]
                    elif res == cnt:
                        if check[0] > check_temp[0]:
                            for i in range(len(check)):
                                check_temp[i] = check[i]
                            for i in range(n):
                                for j in range(n):
                                    temp[i][j] = g_map[i][j]
                        elif check[0] == check_temp[0]:
                            if check[1] > check_temp[1]:
                                for i in range(len(check)):
                                    check_temp[i] = check[i]
                                for i in range(n):
                                    for j in range(n):
                                        temp[i][j] = g_map[i][j]
                            elif check[1] == check_temp[1]:
                                if check[2] > check_temp[2]:
                                    for i in range(len(check)):
                                        check_temp[i] = check[i]
                                    for i in range(n):
                                        for j in range(n):
                                            temp[i][j] = g_map[i][j]
                
    if flag:
        break
    for y in range(n):
        for x in range(n):
            if temp[y][x] == 1:
                g[y][x] = 'x'
    score += res ** 2
    # print(score)
    # print("%d--------remove--------"%s)
    # for x in g:
    #     print(x)
    gravity(g)
    # print("%d--------gravity--------" %s)
    # for x in g:
    #     print(x)
    g = rotate()
    # print("%d--------rotate--------" % s)
    # for x in g:
    #     print(x)
    gravity(g)
    # print("%d--------gravity--------" % s)
    # for x in g:
    #     print(x)
    # print()
print(score)
