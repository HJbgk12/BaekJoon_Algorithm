import sys
from collections import deque

T = int(sys.stdin.readline())

def topology_sort():
    result = []
    time = [0] * (n+1)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            time[i] = d[i-1]
    while q:
        now = q.popleft()
        result.append(now)
        for x in g[now]:
            indegree[x] -= 1
            time[x] = max(time[now]+d[x-1],time[x])
            if indegree[x] == 0:
                q.append(x)
    return time

for i in range(T):
    n, k = map(int, sys.stdin.readline().split())
    d = list(map(int, sys.stdin.readline().split()))
    g = [[] for i in range(n+1)]
    indegree = [0]*(n+1)
    for j in range(k):
        x,y = map(int, sys.stdin.readline().split())
        g[x].append(y)
        indegree[y] += 1
    w = int(sys.stdin.readline())
    print(topology_sort()[w])

