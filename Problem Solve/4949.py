import sys
from collections import deque

while True:
    x = sys.stdin.readline().rstrip()
    flag = 0
    if x == '.':
        break
    else:
        s = deque(x)
        temp = []
        while s:
            x = s.popleft()
            if x == '(' or x == '[':
                temp.append(x)
            elif x == ')':
                if temp:
                    y = temp.pop()
                    if y != '(':
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            elif x == ']':
                if temp:
                    y = temp.pop()
                    if y != '[':
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            else:
                continue
        if flag or temp:
            print("no")
        else:
            print("yes")
