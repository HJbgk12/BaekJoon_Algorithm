import sys
n = int(input())
h = [[0 for _ in range(3)]for _ in range(n+1)]
rgb = [[0 for _ in range(3)]for _ in range(n+1)]
for i in range(1,n+1):
    r,g,b = (map(int, sys.stdin.readline().split()))
    rgb[i][0],rgb[i][1],rgb[i][2] = r,g,b
for i in range(1,n+1):
    h[i][0] = min(h[i - 1][1], h[i - 1][2]) + rgb[i][0]
    h[i][1] = min(h[i - 1][0], h[i - 1][2]) + rgb[i][1]
    h[i][2] = min(h[i - 1][0], h[i - 1][1]) + rgb[i][2]
print(min(h[n]))