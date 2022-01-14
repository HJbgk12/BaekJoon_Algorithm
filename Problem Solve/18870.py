import sys

n = int(input())
point = list(map(int, sys.stdin.readline().split()))
temp_point = sorted(set(point))
dict_point = {p:idx for idx,p in enumerate(temp_point)}

for p in point:
    print(dict_point[p],end = ' ')