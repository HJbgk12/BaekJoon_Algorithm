import sys
sys.setrecursionlimit(10**6)
def nCr(n,r):

    if r == 0:
        return 1
    if n < r:
        return 0
    if n < 0 or 1000 < n or r < 0 or 1000 < r:
        return 0
    if cache[n][r] != -1:
        return cache[n][r]
    tmp = (nCr(n-1,r-1) + nCr(n-1,r)) % 10007
    cache[n][r] = tmp
    return cache[n][r]



cache = [[0 for _ in range(1001)]for _ in range(1001)]

for i in range(1001):
    for j in range(1001):
        cache[i][j] = -1
n,k = map(int, input().split())
print(nCr(n,k))