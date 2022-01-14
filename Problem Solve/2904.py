n = int(input())
num = list(map(int, input().split()))

che = [0]*1000001 # 1000000이하의 소수판별리스트
prime = [] # 판별된 소수저장리스트
count = [[0 for _ in range(80000)]for _ in range(n)]
totcount = [0 for _ in range(80000)]
gcdcount = [0 for _ in range(80000)]

for i in range(2, 1000000): # i를 2부터가면서 i의 배수들을 체크함
    if che[i]:
        continue
    for j in range(i * 2, 1000000,i):
        che[j] = True

for i in range(2,1000000): # 판별된 소수 저장
    if not che[i]:
        prime.append(i)

# 각 숫자별로 소수가 몇개씩 있을까? => 소인수분해
for i in range(n):
    k = num[i]
    for j in range(len(prime)):
        while k % prime[j] == 0:
            count[i][j] += 1
            totcount[j]+=1
            k /= prime[j]

for i in range(len(prime)):
        gcdcount[i] = totcount[i] // n
res1 = 1
res2 = 0
for i in range(len(prime)):
    for j in range(gcdcount[i]):
        res1 *= prime[i]
        # 각 숫자들에 대해서 gcd가 되기 위해 소수가 얼마나 부족한지 확인
    for j in range(n):
        if count[j][i] < gcdcount[i]:
            res2 += gcdcount[i] - count[j][i]

print(res1,res2)
