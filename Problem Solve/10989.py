import sys
idx = [0 for _ in range(10001)]
for i in range(int(input())):
    idx[int(sys.stdin.readline())] += 1
for i in range(len(idx)):
    for j in range(idx[i]):
          print(i)