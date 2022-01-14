import sys
from collections import deque

def order(s):
    x = s.split(' ')
    if x[0] == 'push':
        dq.append(int(x[1]))
    elif x[0] == 'pop':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(dq))
    elif x[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif x[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif x[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)


dq = deque()
n = int(input())
for i in range(n):
    s = sys.stdin.readline().strip()
    order(s)