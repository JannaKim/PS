N, M = map(int, input().split())
mp=[]
mp.append([1]*(M+2))
for _ in range(N):
    mp.append([1]+[int(i) for i in input()]+[1])
mp.append([1]*(M+2))

# [print(i) for i in mp]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(i,j):
    mp[i][j]=1
    for x, y in zip(dx,dy):
        if mp[i+x][j+y]==0:
            dfs(i+x,j+y)


cnt=0
for i in range(1,N+1):
    for j in range(1,M+1):
        if mp[i][j]==0:
            
            dfs(i,j)
            cnt+=1

print(cnt)
'''
4 5
00110
00011
11111
00000
'''



