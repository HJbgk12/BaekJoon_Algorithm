def dfs(v,s):
    if v == l:
        for x in res:
            if x in moeum:
                break
        else:
            return
        cnt = 0
        for y in res:
            if y in chaeum:
                cnt += 1
            if cnt == 2:
                for z in res:
                    print(z, end='')
                print()
                return

    else:
        for i in range(s,c):
            res[v] = (pw[i])
            dfs(v+1,i+1)



l,c = map(int,input().split())
pw = list(input().split())
pw.sort()
moeum = ['a','e','i','o','u']
chaeum = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
res = [0] * l

dfs(0,0)