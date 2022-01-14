import sys

n = int(input())
point = []
for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    point.append([y,x])
point = sorted(point)
for p in point:
    print(p[1],p[0])