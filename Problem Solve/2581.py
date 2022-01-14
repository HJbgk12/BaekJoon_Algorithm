import sys
import math

m = int(input())
n = int(input())

if m == 1:
    x = [i for i in range(m+1, n + 1)]
else:
    x = [i for i in range(m, n + 1)]
k = list(filter(lambda a:all(a%j for j in range(2,round(math.sqrt(a)+1))) ,x))
if k:
    print(sum(k))
    print(min(k))
else:
    print("-1")

