import sys

n = int(input())
l = []
for i in range(n):
    w,h = map(int, sys.stdin.readline().split())
    l.append([w,h])
rank = [1 for i in range(n)]
for i in range(n):
    rank[i] = 1
    for j in range(n):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            rank[i] += 1
for x in rank:
    print(x, end = ' ')

