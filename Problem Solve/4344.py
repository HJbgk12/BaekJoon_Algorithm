import sys

c = int(input())
for i in range(c):
    stu = list(map(int, sys.stdin.readline().split()))
    avg = sum(stu[1:])/stu[0]
    cnt = 0
    for x in stu[1:]:
        if x > avg:
            cnt += 1
    print("{:.3f}%".format(round(cnt*100/stu[0],3)))