word = input()
alpha = [0]*26
for x in word:
    alpha[ord(x.lower())-97] += 1

if alpha.count(max(alpha)) == 1:
    print(chr((alpha.index(max(alpha))+97)).upper())
else:
    print('?')