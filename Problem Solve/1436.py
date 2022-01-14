import sys
n = int(input())
x = 666
while n:
    if '666' in str(x):
        n -= 1
        if n == 0:
            break
    x += 1
print(x)