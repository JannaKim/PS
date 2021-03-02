n= int(input())

road= [[*map(int, input().split())] for _ in range(n)]


chk= [False]*n
def topdown(i):

    if all(chk[1:]):
        return road[i][0] or 1e9

    ans= 1e9
    for j in range(1,n):
        if not chk[j] and road[i][j]:
            chk[j]=True
            tmp= topdown(j)
            chk[j]=False
            ans= min(ans, tmp+road[i][j])

    return ans


print(topdown(0))

