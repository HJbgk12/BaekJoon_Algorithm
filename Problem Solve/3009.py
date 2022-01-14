import sys

a = [0 for i in range(1001)]
b = [0 for i in range(1001)]
point = []
for i in range(3):
    x,y = map(int, sys.stdin.readline().split())
    point.append([x,y])
    a[x] += 1
    b[y] += 1
for p in point:
    if a[p[0]] == 1:
        x = p[0]
    if b[p[1]] == 1:
        y = p[1]
print(x,y)