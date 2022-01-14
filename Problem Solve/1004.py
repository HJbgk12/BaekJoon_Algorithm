import sys

T = int(input())

for i in range(T):
    s_x,s_y,e_x,e_y = map(int, input().split())
    n = int(input())
    planet = []
    cnt = 0
    for j in range(n):
        a,b,r = map(int, input().split())
        if (s_x-a)**2 + (s_y-b)**2 < r**2:
            cnt += 1
        if (e_x-a)**2 + (e_y-b)**2 < r**2:
            cnt += 1
        if (s_x-a)**2 + (s_y-b)**2 < r**2 and (e_x-a)**2 + (e_y-b)**2 < r**2:
            cnt -= 2
    print(cnt)