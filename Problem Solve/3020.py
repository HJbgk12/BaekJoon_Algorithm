# 개똥벌레

# def check_seok(k, x): # x구간으로 날아갈때 k번째 석순과 만나는지
#     if x <= seok[k]:
#         return True
#     return False
# def check_jong(k, x):  # x구간으로 날아갈때 k번째 종유석과 만나는지
#     global h
#     if h - jong[k] + 1 <= x:
#         return True
#     return False
#
# def fly(x):
#     res = 0
#     global n
#     for i in range(0,n,2):
#         # 석순과 만나는지
#         if check_seok(i,x):
#             res += 1
#         # 종유석과 만나는지
#         if check_jong(i,x):
#             res += 1
#     # 시간이 오래 걸림
#     # 구간에서 만나는 판단을 빠르게 할 수 없을까?
#     # 1. 정렬하고 누적시킴 => 누적합 사용
#     # 2. +1, -1, ......
#     return res

n,h = map(int, input().split())
# seok = [0]*(200000)
# jong = [0]*(200000)
tot = [0]*(h+10)
answer = -1
count = 0
for i in range(n):
    bar = int(input())
    if i & 1:#종유석  짝수판별
        tot[h-bar+1] += 1
    else:#석순
        tot[1] += 1
        tot[bar + 1] -= 1

for i in range(1,h+1):
    tot[i] += tot[i-1]
    if answer == -1 or tot[i] < answer:
        answer = tot[i]
        count = 1
    elif tot[i] == answer:
        count += 1
print(answer,count)
# for i in range(1,h+1):
#     crash = fly(i)
#     if answer == -1 or crash < answer:
#         answer = crash
#         count = 1
#     elif crash == answer:
#         count += 1