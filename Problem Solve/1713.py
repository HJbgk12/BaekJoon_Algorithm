import sys
from collections import deque

n = int(input())

recommand = int(input())

student = deque(map(int, input().split()))

pic = []
old = [0 for _ in range(1001)]
cnt = [0 for _ in range(1001)]
time = 1000000
tot = 0
while student:
    x = student.popleft()

    time -= 1
    if not pic:
        pic.append(x)
        old[x] = time
        cnt[x] += 1
        tot += 1

    else:

        if tot < n:
            if x in pic:
                cnt[x] += 1
                

            else:
                pic.append(x)
                cnt[x] += 1
                old[x] = time
                tot += 1


        else:

            if x in pic:
                cnt[x] += 1
         
                
            else:

                mn = 1000000
                mx = 0
                mn_idx = []

                for i in range(len(pic)):
                    if cnt[pic[i]] != 0 and cnt[pic[i]] < mn:
                        mn = cnt[pic[i]]
                for i in range(len(pic)):
                    if cnt[pic[i]] == mn:
                        mn_idx.append(i)
                if len(mn_idx) <= 1:
                    old[pic[mn_idx[0]]] = 0
                    cnt[pic[mn_idx[0]]] = 0
                    pic.pop(mn_idx[0])
                    pic.append(x)
                    cnt[x] += 1
                    old[x] = time


                else:
                    for k in mn_idx:
                        if old[pic[k]] > mx:
                            mx = old[pic[k]]
                            mx_idx = k
                    old[pic[mx_idx]] = 0
                    cnt[pic[mx_idx]] = 0
                    pic.pop(mx_idx)
                    pic.append(x)
                    old[x] = time
                    cnt[x] += 1

pic.sort()
for x in pic:
    print(x,end = ' ')
