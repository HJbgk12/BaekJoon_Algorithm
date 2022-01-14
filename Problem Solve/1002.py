import sys
import math

T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    mx = max(r1,r2)
    mn = min(r1,r2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print("-1")
        elif r1 != r2:
            print("0")
    else:
        if r1+r2 < d or mx > mn + d:
            print("0")
        elif d == (r1 + r2) or mx == mn + d:
            print("1")
        elif d < r1 + r2:
            print("2")