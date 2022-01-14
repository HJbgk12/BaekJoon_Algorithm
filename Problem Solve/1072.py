x,y = map(int, input().split())
z = int(y * 100 / x)
if x == y or z == 100 or z == 99:
    print(-1)
else:
    #이분탐색으로 진행
    bottom= 1
    top = 1000000000
    ans = 1000000000
    while bottom <= top:
        mid = (bottom + top) // 2
        nextZ = int((y+mid) * 100 / (x + mid))
        if z < nextZ:
            if mid < ans:
                ans = mid
            top = mid - 1
        else:
            bottom = mid + 1

    print(ans)