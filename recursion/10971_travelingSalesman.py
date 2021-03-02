n= int(input())

L=[[*map(int, input().split())] for _ in range(n)]

chk= [False]*n
def td(i):
    if all(chk[1:]):
        return L[i][0] or 1e9

    ans= 1e9
    for j in range(1,n):
        if not chk[j] and L[i][j]: # 만약 길이 있다면
            chk[j]=True
            tmp= td(j)
            chk[j]=False
            ans= min(ans, tmp+L[i][j])
    
    return ans

print(td(0))