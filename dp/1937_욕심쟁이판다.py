import sys
sys.setrecursionlimit(25000)

n = int(input())
mp=[]
mp.append([0]*(n+2))
for _ in range(n):
    mp.append([0]+[int(i) for i in input().split()]+[0])

mp.append([0]*(n+2))

#[print(f"{line[i]:>3}",end=('\n' if i+1==len(line) else ' ')) for line in mp for i in range(len(line))]

dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]


dp=[]
[dp.append([-1]*(n+2)) for _ in range(n+2)]

def f(i,j):
    
    if dp[i][j]!=-1:
        return dp[i][j]
    dp[i][j]=0
    if i==0 or j==0 or i==n+1 or j==n+1:
        return 0
    for x, y in zip(dx,dy):
            dp[i][j] = max(dp[i][j], 1+ (f(i+x,j+y) if mp[i+x][j+y]<mp[i][j] else 0))
            '''
            if mp[i+x][j+y]<mp[i][j]:
                dp[i][j] = max(dp[i][j], f(i+x,j+y) +1)
            '''
            
    return dp[i][j]
mx=0
for i in range(1,n+1):
    for j in range(1,n+1):
        mx = max(mx, f(i,j))

#print()      
#[print(f"{line[i]:>3}",end=('\n' if i+1==len(line) else ' ')) for line in dp for i in range(len(line))]
print(mx)
                

''' 
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8

5
2 1 2 1 2
1 2 1 2 1
2 1 2 1 2
1 2 1 2 1
2 1 2 1 2
'''
