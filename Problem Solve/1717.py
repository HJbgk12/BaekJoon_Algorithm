import sys
sys.setrecursionlimit(10**6)
def find(n):
    if p[n] == n:
        return n
    p[n] = find(p[n])
    return p[n]

def union(a,b, bond):
    c = find(a)
    d = find(b)
    if c == d:
        return 1
    if bond:
        p[c] = d
    return 0


n,m = map(int, input().split())
num = [[-1]for _ in range(n+1)]
p = [0] * (n+1)
for i in range(n+1):
    p[i] = i
for i in range(m):
    x,a,b = map(int, sys.stdin.readline().strip().split())
    if x == 0:
        union(a,b,1)
    if x == 1:
        if union(a,b,0):
            print("YES")
        else:
            print("NO")