import sys
mx = 0
cnt = 0
while True:
    try:
        n = int(sys.stdin.readline())
        cnt += 1
        if mx < n:
            mx = n
            idx = cnt
    except:
        print(mx,idx)
        break