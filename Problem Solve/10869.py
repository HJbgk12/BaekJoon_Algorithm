import sys

a,b = map(int, sys.stdin.readline().split())


print(a+b)
print(a-b)
print(a*b)
if b!=0:
    print(a//b)
    print(a%b)
else:
    print(0)
    print(0)