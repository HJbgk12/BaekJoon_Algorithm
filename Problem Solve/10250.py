import sys

t = int(input())
for i in range(t):
    h,w,n = map(int, sys.stdin.readline().split())
    c_w = n // h + 1
    if not n%h:
        c_h = h
        c_w -= 1
    else:
        c_h = n%h

    if c_w < 10:
        res = str(c_h)+'0'+str(c_w)
    else:
        res = str(c_h) + str(c_w)
    print(res)
