n = int(input())
num = list(map(int, input().split()))

che = [0]*1000001 # 1000000������ �Ҽ��Ǻ�����Ʈ
prime = [] # �Ǻ��� �Ҽ����帮��Ʈ
count = [[0 for _ in range(80000)]for _ in range(n)]
totcount = [0 for _ in range(80000)]
gcdcount = [0 for _ in range(80000)]

for i in range(2, 1000000): # i�� 2���Ͱ��鼭 i�� ������� üũ��
    if che[i]:
        continue
    for j in range(i * 2, 1000000,i):
        che[j] = True

for i in range(2,1000000): # �Ǻ��� �Ҽ� ����
    if not che[i]:
        prime.append(i)

# �� ���ں��� �Ҽ��� ��� ������? => ���μ�����
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
        # �� ���ڵ鿡 ���ؼ� gcd�� �Ǳ� ���� �Ҽ��� �󸶳� �������� Ȯ��
    for j in range(n):
        if count[j][i] < gcdcount[i]:
            res2 += gcdcount[i] - count[j][i]

print(res1,res2)
