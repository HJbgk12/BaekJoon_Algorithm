import sys
from collections import deque

def order(s):
    x = str(s)
    k = x.split(' ')
    if x[0] == 'p' and x[1] == 'u':
        dq.append(int(k[-1]))
    elif x[0] == 'p' and x[1] == 'o':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())

    elif x[0] == 's':
        print(len(dq))
    elif x[0] == 'e':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 't':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])

n = int(input())
dq = deque()
for i in range(n):
    s = sys.stdin.readline().strip()
    order(s)
