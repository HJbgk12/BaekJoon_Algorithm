import sys
def dfs(v, l):
    global mn
    if v == m:
        res1 = list(set(p) - set(res))
        temp = 0
        for i in range(m):
            for j in range(m):
                temp += s[res1[i]-1][res1[j]-1]-s[res[i]-1][res[j]-1]
        mn = min(mn,abs(temp))
        return
    else:
        for i in range(l,n+1):
            res[v] = i
            dfs(v+1, i+1)
n = int(input())
s = []
for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    s.append(x)
p = [i for i in range(1,n+1)]
m = n//2
res = [0 for _ in range(n//2)]
mn = 10000000
dfs(0, 1)
print(mn)