a,b,c = map(int, input().split())
x = 1
if c <= b:
    x = -1
else:
    x = a//(c-b) + 1
print(x)