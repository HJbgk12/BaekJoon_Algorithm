# ���˹���

# def check_seok(k, x): # x�������� ���ư��� k��° ������ ��������
#     if x <= seok[k]:
#         return True
#     return False
# def check_jong(k, x):  # x�������� ���ư��� k��° �������� ��������
#     global h
#     if h - jong[k] + 1 <= x:
#         return True
#     return False
#
# def fly(x):
#     res = 0
#     global n
#     for i in range(0,n,2):
#         # ������ ��������
#         if check_seok(i,x):
#             res += 1
#         # �������� ��������
#         if check_jong(i,x):
#             res += 1
#     # �ð��� ���� �ɸ�
#     # �������� ������ �Ǵ��� ������ �� �� ������?
#     # 1. �����ϰ� ������Ŵ => ������ ���
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
    if i & 1:#������  ¦���Ǻ�
        tot[h-bar+1] += 1
    else:#����
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