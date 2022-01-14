import sys

n = int(input())
step = [int(sys.stdin.readline()) for _ in range(n)]
if n == 1:
    print(step[0])
elif n == 2:
    print(step[0]+step[1])
else:
    d = [[0 for _ in range(2)] for _ in range(n + 1)]
    if n <= 3:
        t = 3
    else:
        t = 1
    d[0][0] = step[0]
    d[0][1] = 0
    flag = 0
    for i in range(1, n):
        if flag < t:
            flag += 1
            d[i][0] = max(d[i - 1][0],d[i-1][1]) + step[i]
        else:
            flag = 0
            d[i][0] = d[i-1][1] + step[i]
        if flag < 2:
            flag += 1
            d[i][1] = max(d[i-2][0],d[i-2][1]) + step[i]
        else:
            flag = 0
            d[i][1] = d[i-2][1] + step[i]
    print(max(d[n - 1]))