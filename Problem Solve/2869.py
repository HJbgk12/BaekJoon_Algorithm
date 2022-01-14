a,b,v = map(int, input().split())
n = 2

if v == a:
    print(1)
else:
    if (v-b)%(a-b):
        print((v-b)//(a-b)+1)
    else:
        print((v-b)//(a-b))