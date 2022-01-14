import sys

n = int(input())
t = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0 and t:
        t.pop()
    elif x == 0 and not t:
        continue
    else:
        t.append(x)
print(sum(t))


