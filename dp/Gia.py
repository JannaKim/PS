

def solution(L):
    floor= len(L)
    dp= [[-1e9]*len(L) for _ in range(len(L))]
    for r in range(floor):
        c, val= L[r]
        dp[r][c]=val

    [print(*el) for el in dp]
    def topdown(r,c):
        print(r,c)
        if dp[r][c]!=-1e9:
            return dp[r][c]
        if r==c:
            dp[r][c]= topdown(r-1,c-1)-topdown(r,c-1)
            return dp[r][c]
        else:
            dp[r][c]= topdown(r-1,c)-topdown(r,c+1)
            return dp[r][c]
        

    for i in range(len(L)):
        for j in range(i+1):
            topdown(i,j)

    ans=[]
    for i in range(len(L)):
        for j in range(i+1):

            ans.append(dp[i][j])

    return ans




print(solution([[0,50], [0,22], [1,4], [3,33]]))