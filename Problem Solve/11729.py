import sys
sys.setrecursionlimit(10**6)

def dfs(n,s,t,e):
    global cnt
    cnt += 1
    if n == 1:
        res.append([s,e])
        return
    else:
        dfs(n-1, s,e,t)
        res.append([s,e])
        dfs(n-1, t,s,e)

n = int(input())
cnt = 0
res = []
dfs(n,1,2,3)
print(cnt)
for x in res:
    print(x[0],x[1])
