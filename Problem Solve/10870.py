import sys
#sys.setrecursionlimit(10**6)
def dfs(n):
    if x[n]:
        return x[n]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    x[n] = x[n-1]+x[n-2]
    return dfs(n-1)+dfs(n-2)

n = int(input())
x = [0 for i in range(n+1)]
print(dfs(n))