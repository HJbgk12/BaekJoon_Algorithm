import sys
n = int(input())
people = []
for i in range(n):
    people.append(list(sys.stdin.readline().split())+[i])
people = sorted(people, key = lambda x : (int(x[0]),x[2]))
for p in people:
    print(p[0],p[1])