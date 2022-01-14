import sys

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = input()
cnt = 0
tot = 0
flag = 0
word = ''
for i in range(len(s)):
    cnt += 1
    if s[i] == '=':
        if s[i-1] == 'z':
            if i >= 2 and s[i-2] == 'd':
                # print(s[i-2]+s[i-1]+s[i])
                cnt -= 2
            else:
                # print(s[i - 1] + s[i])
                cnt -= 1
        elif s[i-1] == 'c' or s[i-1] == 's':
            # print(s[i - 1] + s[i])
            cnt -= 1
    elif s[i] == '-':
        if s[i-1] == 'c' or s[i-1] == 'd':
            # print(s[i - 1] + s[i])
            cnt -= 1
    elif s[i] == 'j':
        if s[i-1] == 'n' or s[i-1] == 'l':
            # print(s[i - 1] + s[i])
            cnt -= 1


print(cnt)










