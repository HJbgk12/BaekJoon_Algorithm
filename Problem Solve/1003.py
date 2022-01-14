import sys


T = int(input())

def Count(n):
    if cnt[n]:
        return cnt[n]
    if n == 0:
        cnt[0] = 0
        return 1
    elif n == 1:
        cnt[1] = 1
        return 0
    else:
        cnt[n] = Count(n-1) + Count(n-2)
        return cnt[n]


cnt = [0]*42
Count(41)

for i in range(T):
    n = int(input())
    if n == 0:
        print(1,0)
    elif n == 1:
        print(0,1)
    else:
        print(cnt[n-1],cnt[n])



