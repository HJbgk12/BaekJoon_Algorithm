import sys
T =int(input())
for i in range(T):
    r, s = sys.stdin.readline().split()
    p = [int(r)*x for x in s]
    print(''.join(p))