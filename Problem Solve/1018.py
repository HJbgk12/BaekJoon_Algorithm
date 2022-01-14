import sys

n,m = map(int, input().split())
g = []
chess1 = [['B' if i%2 == 0 else 'W' for i in range(8)] if j%2 == 0 else ['B' if i%2 == 1 else 'W' for i in range(8)] for j in range(8)]
chess2 = [['B' if i%2 == 1 else 'W' for i in range(8)] if j%2 == 0 else ['B' if i%2 == 0 else 'W' for i in range(8)] for j in range(8)]

for i in range(n):
    g.append(list(input()))
res = 65
for i in range(n-7):
    for j in range(m-7):
        l1 = []
        l2 = []
        for k in range(8):
            l1 += [1 if x != y else 0 for x,y in zip(chess1[k],g[i+k][j:j+8])]
            l2 += [1 if x != y else 0 for x,y in zip(chess2[k],g[i+k][j:j+8])]
        res = min(min(sum(l1),sum(l2)),res)
print(res)

