import sys

num = [0 for i in range(123456*2+1)]
prime = []
for i in range(2, len(num)):
    if not num[i]:
        prime.append(i)
        for j in range(i, len(num), i):
            num[j] = 1

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    cnt = 0
    for x in prime:
        if n < x <= 2*n:
            cnt += 1
        if x > 2*n:
            break
    print(cnt)




