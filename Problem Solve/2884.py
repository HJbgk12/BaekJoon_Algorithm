import sys
h,m = map(int, sys.stdin.readline().split())

h -= 1
m += 15
if 60 <= m <= 75:
    if h < 0:
        h = 23
    h += 1
    if h == 24:
        h = 0
    m -= 60
    print(h, m)
else:
    if h < 0:
        h = 23
    print(h,m)

