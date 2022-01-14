import sys
n = int(input())
num = list(map(int, input().split()))
flag = list(map(int, input().split()))

def dfs(v,tot):
    global mx,mn
    if v == n-1:
        mx = max(mx,tot)
        mn = min(mn,tot)
        return
    else:
        for i in range(4):
            if flag[i]:
                flag[i] -= 1
                if i == 0:
                    dfs(v + 1, tot + num[v + 1])
                elif i == 1:
                    dfs(v + 1, tot - num[v + 1])
                elif i == 3:
                    if tot < 0:
                        dfs(v + 1, -(-tot // num[v + 1]))
                    else:
                        dfs(v + 1, tot // num[v + 1])
                else:
                    dfs(v + 1, tot * num[v + 1])
                flag[i] += 1

mx = -1000000001
mn = 1000000001
dfs(0,num[0])
print(mx)
print(mn)