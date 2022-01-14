import sys
import itertools
import math


t = int(sys.stdin.readline())




for _ in range(t):
    p = []
    v = []
    tot_x = 0
    tot_y = 0

    n = int(sys.stdin.readline())
    for _ in range(n):
        x,y = map(int, sys.stdin.readline().split())
        p.append([x,y])
        tot_x += x
        tot_y += y
    ret = sys.maxsize # max°ª ÁöÁ¤
    combi = list(itertools.combinations(p, int(n/2)))
    combi_len = int(len(combi)/2)

    for element in combi[:combi_len]:
        element = list(element)
        x1_tot = 0
        y1_tot = 0
        for x1, y1 in element:
            x1_tot += x1
            y1_tot += y1
        x2_tot = tot_x - x1_tot
        y2_tot = tot_y - y1_tot

        ret = min(ret, math.sqrt((x1_tot- x2_tot)**2 + (y1_tot - y2_tot)**2))
    print(ret)
