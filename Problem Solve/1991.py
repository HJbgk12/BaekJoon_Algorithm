import sys
def fdfs(s, v):
    if s == len(tree):
        return
    else:
        if v == tree[s][0]:
            print(tree[s][1], end = '')
            fdfs(s+1, v*2 + 1)
            fdfs(s+1, v*2 + 2)
        else:
            fdfs(s+1, v)


def mdfs(s, v):
    if s == len(tree):
        return
    else:
        if v == tree[s][0]:
            mdfs(s+1, v * 2 + 1)
            print(tree[s][1], end = '')
            mdfs(s+1, v * 2 + 2)
        else:
            mdfs(s+1,v)

def bdfs(s,v):
    if s == len(tree):
        return
    else:
        if v == tree[s][0]:
            bdfs(s + 1, v * 2 + 1)
            bdfs(s + 1, v * 2 + 2)
            print(tree[s][1], end='')
        else:
            bdfs(s + 1, v)


n = int(input())
x = []
for i in range(n):
    s = sys.stdin.readline().strip()
    x.append(s.split())
tree = []
tree.append([0,'A'])

for i in range(n):
    for j in x:
        if tree[i][1] == j[0]:
            if j[1] != '.':
                tree.append([tree[i][0]*2+1,j[1]])
            if j[2] != '.':
                tree.append([tree[i][0]*2+2,j[2]])

fdfs(0,0)
print()
mdfs(0,0)
print()
bdfs(0,0)

