a = int(input())
b = int(input())
c = int(input())

n = a*b*c
k = [0]*10
for x in str(n):
    k[int(x)] += 1
for i in range(10):
    print(k[i])
