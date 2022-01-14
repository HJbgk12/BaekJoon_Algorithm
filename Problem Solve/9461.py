import sys
for i in range(int(input())):
    a = b = 1
    c = 2
    for j in range(int(sys.stdin.readline())-2):
        a, b, c = b, c, a+b
    print(a)