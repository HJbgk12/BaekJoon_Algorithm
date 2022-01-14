n = int(input())
score = list(map(int, input().split()))
mx = max(score)
print(sum(score)*100/mx/n)
