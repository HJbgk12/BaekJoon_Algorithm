import sys

def rotate(x, d, k):
    for i in range(x, n+1, x):
        if d == 0:
            circle[i-1] = circle[i-1][m-k:] + circle[i-1][:m-k]
        else:
            circle[i-1] = circle[i-1][k:] + circle[i-1][:k]
    if check():
        return 1
    return 0

def check():
    check_cir = [[0 for _ in range(m)]for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(m): # 같은 원안에 인접한 수가 있는지 확인
            if circle[i][j] == circle[i][j-1] and circle[i][j] != 0:
                check_cir[i][j] = 'x'
                check_cir[i][j-1] = 'x'
                flag = 1
    for j in range(m):
        for i in range(n-1):
            if circle[i][j] == circle[i+1][j] and circle[i][j] != 0:
                check_cir[i][j] = 'x'
                check_cir[i+1][j] = 'x'
                flag = 1
    if flag == 0:
        tot = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    tot += circle[i][j]
                    cnt += 1
        if cnt != 0:
            avg = float(tot / cnt)
        else:
            return 0
        for i in range(n):
            for j in range(m):
                if circle[i][j] != 0:
                    if circle[i][j] > avg:
                        circle[i][j] -= 1
                    elif circle[i][j] < avg:
                        circle[i][j] += 1
    else:
        for i in range(n):
            for j in range(m):
                if check_cir[i][j] == 'x':
                    circle[i][j] = 0
    return 1

n,m,t = map(int, sys.stdin.readline().split())
circle = []
for i in range(n):
    circle.append(list(map(int, sys.stdin.readline().split())))
for i in range(t):
    x, d, k = map(int, sys.stdin.readline().split())
    if not rotate(x, d, k):
        break
res = 0
for i in range(n):
    res += sum(circle[i])
print(res)
