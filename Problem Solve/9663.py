def nqueen(k,c):
    global cnt
    if k == n:
        cnt +=1
    else:
        for i in range(n):
            if g[k][i] == -1 and check[i] == 0:
                g[k][i] = 1
                check[i] = 1
                for j in range(n):
                    if g[k][j] == -1:
                        g[k][j] = c
                    if k+j+1 < n:
                        if g[k+j+1][i] == -1:
                            g[k+j+1][i] = c
                        if i+j+1 < n and g[k+j+1][i+j+1] == -1:
                            g[k+j+1][i+j+1] = c
                        if i-j-1 >= 0 and g[k+j+1][i-j-1] == -1:
                            g[k+j+1][i-j-1] = c
                nqueen(k+1,c+1)
                g[k][i] = -1
                check[i] = 0
                for j in range(n):
                    if g[k][j] == c:
                        g[k][j] = -1
                    if k+j+1 < n:
                        if g[k+j+1][i] == c:
                            g[k+j+1][i] = -1
                        if i+j+1 < n and g[k+j+1][i+j+1] == c:
                            g[k+j+1][i+j+1] = -1
                        if i-j-1 >= 0 and g[k + j + 1][i - j - 1] == c:
                            g[k+j+1][i-j-1] = -1

n = int(input())
g = [[-1 for _ in range(n)]for _ in range(n)]
check = [0 for _ in range(n)]
cnt = 0
nqueen(0,n+1)
print(cnt)