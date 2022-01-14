import sys
from itertools import combinations
n,m = map(int, input().split())
l = list(map(int, input().split()))

comb = list(combinations(l,3))
res = 0
for x in comb:
    if res < sum(x) <= m:
        res = sum(x)
print(res)

