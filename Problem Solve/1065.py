n = int(input())
def Count(n):
    num = str(n)
    if len(num) == 1 or len(num) == 2:
        return 1
    else:
        temp = int(num[1])-int(num[0])
        for i in range(len(num)-1):
            x = int(num[i+1])-int(num[i])
            if temp == x:
                continue
            else:
                return 0
    return 1

cnt = 0
for i in range(1,n+1):
    cnt += Count(i)
print(cnt)