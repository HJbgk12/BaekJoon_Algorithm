n,m = map(int, input().split())

a = list(map(int, input().split()))

ans = 0
sum_m = 0
s = 0
e = 0
tot = 0

while s < n and e < n:
    tot += a[e]
    while tot > m:
        if s == e:
            break
        tot -= a[s]
        s += 1
    if tot == m:
        ans += 1
    e += 1

print(ans)
