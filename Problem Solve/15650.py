def dfs(l,k):
    if k == m:
        for x in res:
            print(x,end = ' ')
        print()
        return
    else:
        for i in range(l, n+1):
            res[k] = i
            dfs(i+1, k + 1)


n,m = map(int, input().split())
res_map = [0 for i in range(1,n+1)]
res = [0 for i in range(m)]
dfs(1,0)