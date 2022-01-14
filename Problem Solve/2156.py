import sys

n = int(input())
r = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(n+2)]
if n == 1:
    print(r[0])
elif n == 2:
    print(r[0]+r[1])
else:
    dp[0] = r[0]
    dp[1] = r[0]+r[1]
    dp[2] = r[1]+r[2]
    for i in range(2,n):
        dp[i] = max(dp[i-1],r[i]+dp[i-2],r[i]+r[i-1]+dp[i-3])
    print(dp[n-1])