import sys

n = int(input())
prime = list(map(int,sys.stdin.readline().split()))

cnt = 0
for i in range(n):
    flag = 1
    if prime[i] == 1:
        continue
    if prime[i] == 2:
        cnt += 1
        continue
    for j in range(2,prime[i]):
        if prime[i] % j == 0:
            flag = 0
            break
    if flag:
        cnt += 1
print(cnt)