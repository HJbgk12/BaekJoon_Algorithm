import sys
sys.setrecursionlimit(10**6)

def dfs(k,u,m,d):
    if k == n:
        for i in u:
            print(i)
        for i in m:
            print(i)
        for i in d:
            print(i)
        return
    else:
        temp = []
        for x in u:
            temp.append(x*3)
        for x in m:
            temp.append(x*3)
        for x in d:
            temp.append(x*3)
        # print(temp)
        u = temp
        temp = []
        for x in m:
            temp.append(x[:(k//3)]*3+x[(k//3):2*(k//3)]*3+x[2*(k//3):]*3)
        for x in m:
            temp.append(x + ' '*(k)+x)
        for x in m:
            temp.append(x[:(k//3)]*3+x[(k//3):2*(k//3)]*3+x[2*(k//3):]*3)
        m = temp
        d = u
        return dfs(k*3,u,m,d)

n = int(input())

u = ['*'*3]
m = ['*'*1+' '*1+'*'*1]
d = ['*'*3]
dfs(3,u,m,d)






