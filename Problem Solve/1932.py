import sys
n = int(input())
temp = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    if i == 0:
        temp[0][0] = l[0]
    else:
        l.append(0)
        for j in range(len(l)-1):
            temp[i][j] = l[j] + max(temp[i-1][j],temp[i-1][j-1])
print(max(temp[n-1]))