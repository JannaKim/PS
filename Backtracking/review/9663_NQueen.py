from time import sleep
n= int(input())
mp= [[0]*n for _ in range(n)]
ans=0
chk= [[0]*n for _ in range(n)]
line=[False]*n
def backtrack(i):
    global ans

    if i==n:
        ans+=1
        [print(*el) for el in mp]
        print()
        #sleep(0.5)
        return
    if i==0:
        for j in range(n):
            chk[i][j]=1
            mp[i][j]=1
            line[j]=True
            ci=i+1
            cj=j+1
            for _ in range(n):
                if ci<n and cj<n:
                    #print(ci,cj)
                    chk[ci][cj]+=1
                else:
                    break
                ci+=1
                cj+=1
            ci=i+1
            cj=j-1
            for _ in range(n):
                if ci<n and 0<=cj:
                    #print(ci,cj)
                    chk[ci][cj]+=1
                else:
                    break 
                ci+=1
                cj-=1
            backtrack(i+1)
            chk[i][j]=0
            line[j]=False
            mp[i][j]
            chk[i][j]-=1
            line[j]=False
            mp[i][j]=0

            ci=i+1
            cj=j+1
            for _ in range(n):
                if ci<n and cj<n:
                    #print(ci,cj)
                    chk[ci][cj]-=1
                else:
                    break
                ci+=1
                cj+=1
            ci=i+1
            cj=j-1
            for _ in range(n):
                if ci<n and 0<=cj: #############
                    #print(ci,cj)
                    chk[ci][cj]-=1
                else:
                    break 
                ci+=1
                cj-=1
    
    else:
        flag=False
        '''
        print(line)
        [print(*el) for el in mp]
        print()
        [print(*el) for el in chk]
        print('chk')
        sleep(0.5)
        '''
        for j in range(n):
            if not line[j]:
                if not chk[i][j]:
                    chk[i][j]+=1
                    line[j]=True
                    ci=i+1
                    cj=j+1
                    for _ in range(n):
                        if ci<n and cj<n:
                            #print(ci,cj)
                            chk[ci][cj]+=1
                        else:
                            break
                        ci+=1
                        cj+=1
                    ci=i+1
                    cj=j-1
                    for _ in range(n):
                        if ci<n and 0<=cj:
                            #print(ci,cj)
                            chk[ci][cj]+=1
                        else:
                            break 
                        ci+=1
                        cj-=1
                    #print('s',s)
                    mp[i][j]=1
                    backtrack(i+1)
                    chk[i][j]-=1
                    line[j]=False
                    mp[i][j]=0

                    ci=i+1
                    cj=j+1
                    for _ in range(n):
                        if ci<n and cj<n:
                            #print(ci,cj)
                            chk[ci][cj]-=1
                        else:
                            break
                        ci+=1
                        cj+=1
                    ci=i+1
                    cj=j-1
                    for _ in range(n):
                        if ci<n and 0<=cj:
                            #print(ci,cj)
                            chk[ci][cj]-=1
                        else:
                            break 
                        ci+=1
                        cj-=1
        #if not flag:
        #    backtrack(i+1)


backtrack(0)
print(ans)