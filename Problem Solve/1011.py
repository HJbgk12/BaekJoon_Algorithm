import sys
import math
# sys.stdin = open("input", "rt")

t = int(input())
for i in range(t):
    x,y = map(int, sys.stdin.readline().split())
    # if y - x == 1:
    #     print("1")
    #     continue
    # else:
    s = 0
    e = y - x
    idx = round(math.sqrt(e))
    if idx**2 - idx < e <= idx**2:
        print(2*idx-1)
    elif idx**2 < e <= idx**2 + idx:
        print(2 * idx)
    else:
        print(2*idx-2)


