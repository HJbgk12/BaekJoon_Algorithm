import sys

x,y,w,h = map(int, sys.stdin.readline().split())

if x >= w:
    if 0 <= y < h:
        print(x-w)
    else:
        print(x-w + min(abs(y-h), abs(-y)))
elif 0 <= x < w:
    if 0 <= y < h:
        print(min(min(x,w-x),min(y,h-y)))
    else:
        print(min(abs(y-h), abs(-y)))
else:
    if 0 <= y < h:
        print(-x)
    else:
        print(-x + min(abs(y-h), abs(-y)))

