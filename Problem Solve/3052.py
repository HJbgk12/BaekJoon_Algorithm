import sys
b = [0]*42
cnt = 0
for i in range(10):
    a = int(sys.stdin.readline())
    if not b[a%42]:
        b[a%42] += 1
        cnt += 1
print(cnt)
