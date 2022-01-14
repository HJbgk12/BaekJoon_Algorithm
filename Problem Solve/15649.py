def dfs(l,k):
    if k == m:
        for x in res:
            print(x,end = ' ')
        print()
        return
    else:
        for i in range(n):
            if res_map[i] == 0:
                res_map[i] = 1
                res[k] = i+1
                dfs(l+1,k+1)
                res[k] = 0
                res_map[i] = 0

n,m = map(int, input().split())
res_map = [0 for i in range(1,n+1)]
res = [0 for i in range(m)]
dfs(1,0)