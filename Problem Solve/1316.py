import sys

n = int(input())
cnt = 0
for i in range(n):
    eng = [0]*26
    word = sys.stdin.readline().rstrip()
    flag = 1
    for i in range(len(word)):
        if eng[ord(word[i])-97] == 0:
            eng[ord(word[i]) - 97] = 1
        else:
            if i >= 1 and word[i-1] == word[i]:
                continue
            else:
                flag = 0
                break
    if flag:
        cnt += 1
print(cnt)