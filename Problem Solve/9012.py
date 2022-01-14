import sys

n = int(input())
for i in range(n):
    vps = list(sys.stdin.readline().strip())
    if vps[0] == ')' or vps[-1] == '(':
        print("NO")
        continue
    else:
        temp = []
        for x in vps:
            if x == '(':
                temp.append('(')
            else:
                if temp:
                    temp.pop()
                else:
                    temp.append(0)
                    break
        if temp:
            print("NO")
        else:
            print("YES")






