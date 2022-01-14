import sys

while True:
    t = list(map(int, sys.stdin.readline().split()))
    if not all(t):
        break
    t.sort(reverse = True)
    if t[0]**2 == t[1]**2 + t[2]**2:
        print("right")
    else:
        print("wrong")