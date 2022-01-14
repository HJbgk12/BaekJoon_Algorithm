import sys

n = int(input())
for i in range(1,n):
    cnt = i
    tmp = i
    while True:
        cnt += (tmp % 10)
        tmp = tmp // 10
        if tmp == 0:
            break
    if cnt == n:
        print(i)
        sys.exit()
print(0)