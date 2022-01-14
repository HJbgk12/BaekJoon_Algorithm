import sys
n = int(input())
word = []
for i in range(n):
    word.append(sys.stdin.readline().rstrip())
word = sorted(set(word), key = lambda x : (len(x),x[:]))
for w in word:
    print(w)