import sys
n = int(input())
l = []
idx = [0 for i in range(8001)]
for i in range(n):
    a = int(sys.stdin.readline())
    l.append(a)
    idx[a] += 1
l.sort()
cnt_mx = max(idx)
res = []
for i in range(len(idx)):
    if idx[i] == cnt_mx:
        if i > 4000:
            res.append(i-8001)
        else:
            res.append(i)
res.sort()
print(round(sum(l)/len(l)))
print(l[len(l)//2])
if len(res) == 1:
    print(res[0])
else:
    print(res[1])
print(max(l)-min(l))