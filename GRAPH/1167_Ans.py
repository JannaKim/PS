import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(250000)
n= int(input())
edge= [[] for _ in range(n+1)]
for _ in range(n):
    line= [*map(int, input().split())]
    for j in range(1,n*2,2):
        if line[j]==-1:
            break
        edge[line[0]].append((line[j], line[j+1]))
    
mx=0
start=0
dp=[0]*(n+1)
def find_start(v):
    flag=False
    for v2, cost in edge[v]:
        if not dp[v2]:
            flag=True
            dp[v2]=dp[v]+cost
            find_start(v2)
    if not flag: # made to end
        #print(v,'made to end')
        global mx, start
        if dp[v]>mx:
            mx= dp[v]
            start= v


find_start(1)   
DP=[0]*(n+1)
DP[start]=1
ans=0
def find_r(v):
    #print(v, v1, accum)
    flag=False
    for v2, cost in edge[v]:
        #print(v2, cost)
        if not DP[v2]:
            flag=True
            DP[v2]=DP[v]+cost
            find_r(v2)
    if not flag: # made to end
        global ans
        ans= max(ans,DP[v])
#print(start)
find_r(start)
#print(DP)
print(ans-1)

#5 4 3
'''
5
1 3 2 -1
2 4 10 -1
3 1 2 4 3 -1
4 2 10 3 3 5 10 -1
5 4 10 -1

10
1 2 1 -1
2 3 1 1 1 -1
3 4 1 2 1 -1
4 5 1 3 1 -1
5 6 1 4 1 -1
6 7 1 5 1 -1
7 8 1 6 1 -1
8 9 1 7 1 -1
9 10 1 8 1 -1
10 9 1 -1
'''