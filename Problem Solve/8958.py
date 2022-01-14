import sys
n = int(input())
for i in range(n):
    ans = list(sys.stdin.readline().rstrip())
    cnt_o = 0
    tot = 0
    for x in ans:
        if x == 'O':
            cnt_o += 1
            tot += cnt_o
        else:
            cnt_o = 0
    print(tot)
