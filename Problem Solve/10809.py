s = input()
al = [-1] * 26

for i,x in enumerate(s):
    if al[ord(x)-97] == -1:
        al[ord(x)-97] = i
for x in al:
    print(x, end = ' ')