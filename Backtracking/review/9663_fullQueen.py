n= int(input())
ans=0
chk= [[0]*n for _ in range(n)]
line=[False]*n
def backtrack(i):
    global ans

    if i==n:
        ans+=1
        return
    
    for j in range(n):
        if not line[j] and not chk[i][j]:
            chk[i][j]+=1
            line[j]=True
            ci=i+1
            cj=j+1
            for _ in range(n):
                if ci<n and cj<n:
                    chk[ci][cj]+=1
                else:
                    break
                ci+=1
                cj+=1
            ci=i+1
            cj=j-1
            for _ in range(n):
                if ci<n and 0<=cj:
                    chk[ci][cj]+=1
                else:
                    break 
                ci+=1
                cj-=1
            backtrack(i+1)
            chk[i][j]-=1
            line[j]=False

            ci=i+1
            cj=j+1
            for _ in range(n):
                if ci<n and cj<n:
                    chk[ci][cj]-=1
                else:
                    break
                ci+=1
                cj+=1
            ci=i+1
            cj=j-1
            for _ in range(n):
                if ci<n and 0<=cj:
                    chk[ci][cj]-=1
                else:
                    break 
                ci+=1
                cj-=1

backtrack(0)
print(ans)