x = int(input())
n = 1
while x > n*(n+1)/2:
    n+=1
if n%2 == 0:
    print("%d/%d"%(int((x-(n*(n-1)/2))),int(n-x+(n*(n-1)/2)+1)))
else:
    print("%d/%d" % (int(n - x + (n * (n - 1) / 2) + 1),int((x - (n * (n - 1) / 2)))))