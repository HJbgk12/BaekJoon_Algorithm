import sys

a,b = map(int, sys.stdin.readline().split())

if b != 0:
    print(a/b)
else:
    print(0)