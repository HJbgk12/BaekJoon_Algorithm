import sys

n = int(input())
heap = []
for i in range(n):
    heap.append(int(sys.stdin.readline()))

def heap_sort(heap):
    for i in range(1, len(heap)):
        c = i
        while c != 0:  # 힙 생성
            root = (c - 1) // 2
            if heap[root] < heap[c]:
                heap[root], heap[c] = heap[c], heap[root]
            c = root

    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        root = 0
        c = 1
        while c < i:
            if heap[c] < heap[c+1] and c < i-1:
                c += 1
            if heap[root] < heap[c] and c < i:
                heap[root], heap[c] = heap[c], heap[root]
            root = c
            c = 2 * root + 1  # 자식중에 더 큰 값 찾기
    for x in heap:
        print(x)
heap_sort(heap)