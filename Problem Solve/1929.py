import sys
import math

m,n = map(int, input().split())
num = [i for i in range(m,n+1)]
for x in num:
    flag = 1
    if x == 1:
        continue
    for i in range(2,round(math.sqrt(x))+1):
        if x % i:
            continue
        else:
            flag = 0
            break
    if flag:
        print(x)