def dfs(l,k):
    if k == m+1:
        for x in res[1:]:
            print(x, end=' ')
        print()
        return
    else:
        for i in range(1, n+1):
            if res[k-1] <= i:
                res[k] = i
                dfs(l+1, k + 1)


n,m = map(int, input().split())
res = [0 for i in range(m+1)]
dfs(1,1)