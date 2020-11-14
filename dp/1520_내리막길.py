M, N = [int(i) for i in input().split()]
# M: 세로
mp=[]
mp.append([0]*(N+2))
for _ in range(M):
    mp.append([0]+[int(i) for i in input().split()]+[0])
mp.append([0]*(N+2))



dp=[]
for _ in range(M+2):
    dp.append([-1]*(N+2))



dx=[0,0,1,-1]
dy=[1,-1,0,0]

dp[1][1]=1

def f(a,b):
    if dp[a][b]!=-1:
        return dp[a][b]
    dp[a][b]+=1
    for x,y in zip(dx,dy):
        if mp[a+x][b+y]>mp[a][b]:
            dp[a][b]+=f(a+x,b+y)
    return dp[a][b]
print(f(M,N))

'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''