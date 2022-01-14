import sys
sys.setrecursionlimit(10**6)

def w(a,b,c):
    if x[a][b][c]:
        return x[a][b][c]
    elif a <= 0 or b <= 0 or c <= 0:
        x[a][b][c] = 1
        return 1
    elif a > 20 or b > 20 or c > 20:
        x[a][b][c] = w(20,20,20)
        return x[a][b][c]
    elif a < b and b < c:
        x[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return x[a][b][c]
    else:
        x[a][b][c] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return x[a][b][c]

x = [[[0 for _ in range(101)] for _ in range(101)]for _ in range(101)]

while True:
    a,b,c = map(int, sys.stdin.readline().split())

    if a == -1 and b == -1 and c == -1:
        sys.exit()
    else:
        print("w(%d, %d, %d) = %d"%(a,b,c,w(a,b,c)))