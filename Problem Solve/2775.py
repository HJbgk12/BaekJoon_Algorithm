import sys

t = int(input())
for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    a = [i for i in range(1, n + 1)]
    a.append(0)
    for i in range(k):
        temp = [0 for _ in range(n+1)]
        for j in range(n):
            temp[j] = sum(a[:j+1])
        a = temp
    print(a[n-1])