dial = {1:[],2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],\
        5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],\
        9:['W','X','Y','Z']}

time = [0,2,3,4,5,6,7,8,9,10]

num = list(input())
res = []
for x in num:
    for i in range(1,len(dial)+1):
        if x in dial[i]:
            res.append(time[i])
            break
print(sum(res))