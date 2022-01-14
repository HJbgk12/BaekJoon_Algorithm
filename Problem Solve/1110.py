n = input()
temp = n
cnt = 0
while True:
    if int(n) < 10:
        n = '0'+n
    n = n[-1] + str(int(n[-2]) + int(n[-1]))[-1]
    cnt += 1
    if int(n) == int(temp):
        break

print(cnt)
