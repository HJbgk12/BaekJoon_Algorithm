import sys

a,b = input().split()
res = 0
for i in range(1,4):
    if int(a[-i]) == int(b[-i]):
        continue
    elif int(a[-i]) > int(b[-i]):
        print(int(a[2]+a[1]+a[0]))
        sys.exit()
    else:
        print(int(b[2]+b[1]+b[0]))
        sys.exit()






