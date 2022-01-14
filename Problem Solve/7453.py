n = int(input())
a = []
b = []
c = []
d = []
ab = [] # a,b 조합
cd = [] # c,d 조합
for i in range(n):
    A,B,C,D = map(int, input().split())
    a.append(A)
    b.append(B)
    c.append(C)
    d.append(D)
# a,b // c,d 합의 조합
for i in range(n):
    for j in range(n):
        ab.append(a[i] + b[j])
        cd.append(c[i] + d[j])

ab.sort()
cd.sort()

# 전략1 map사용
# 전략2 정렬
# 전략 2-1 lower_boud, upper_boud 알아볼 것
# 전략 2-2 안쓰고 ==>

def one():
    p_ab = 0
    p_cd = len(cd) - 1
    cnt = 0
    res = 0
    for i in range(len(ab)):
        target = -ab[i]

        if 0 < i and (ab[i] == ab[i - 1]):
            res += cnt
        else:
            while 0 <= p_cd and target < cd[p_cd]:
                p_cd -= 1
            cnt = 0
            while 0 <= p_cd and target == cd[p_cd]:
                cnt += 1
                p_cd -= 1
            res += cnt
    return res
print(one())