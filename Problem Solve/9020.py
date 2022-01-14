import sys

num = [0 for i in range(10001)]
prime = []
for i in range(2, len(num)):
    if not num[i]:
        prime.append(i)
        for j in range(i, len(num), i):
            num[j] = 1

t = int(input())
for i in range(t):
    n = int(sys.stdin.readline())
    mn = 10000
    for j in range(n//2,0,-1):
        if j in prime and n-j in prime:
            print(j,n-j)
            break