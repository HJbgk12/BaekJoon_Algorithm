import sys

n = int(input())
point = []
for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    point.append([x,y])
point = sorted(point)
for p in point:
    print(p[0],p[1])
