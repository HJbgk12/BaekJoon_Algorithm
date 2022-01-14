a = [0]*10001
def solve(n):
    num = str(n)
    tot = n
    for x in num:
        tot += int(x)
    return tot

for i in range(1,10001):
    n = solve(i)
    if n > 10000:
        continue
    else:
        a[n] = 1
for i in range(1,10001):
    if a[i] == 0:
        print(i)