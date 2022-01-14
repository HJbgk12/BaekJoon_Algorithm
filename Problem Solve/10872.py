import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    if x[n]:
        return n
    if n == 1:
        return 1
    if n == 2:
        return 2
    x[n] = n
    return x[n]*dfs(n-1)

n = int(input())
if n == 0:
    print("1")
    sys.exit()
x = [0 for i in range(n+1)]
print(dfs(n))



