import sys; input= lambda: sys.stdin.readline().rstrip()
from heapq import heappush, heappop
from itertools import combinations as combi
n, m= map(int, input().split())

country= [[*map(int, input().split())] for _ in range(n)]
chk=[[False for _ in range(m)] for _ in range(n)]
Dy=[0,0,1,-1]
Dx=[1,-1,0,0]
cnt=0
dic={}
def dfs(y,x):
    global cnt
    for dy,dx in zip(Dy, Dx):
        ny,nx= y+dy, x+dx
        if 0<=ny<n and 0<=nx<m:
            if not chk[ny][nx] and country[ny][nx]:
                chk[ny][nx]=True
                dic[cnt].append((ny,nx))
                dfs(ny,nx)


for i in range(n):
    for j in range(m):
        if country[i][j] and not chk[i][j]:
            cnt+=1
            dic[cnt]=[]
            dic[cnt].append((i,j))
            chk[i][j]=True
            dfs(i,j)

bridge=[]
for el in combi(list(range(1,cnt+1)),2):
    #print(el)
    left,right= el
    A= dic[left]
    a=len(A)
    B= dic[right]
    b=len(B)
    for i in range(a):
        for j in range(b):
            y1, x1= A[i]
            y2, x2= B[j]
            if y1==y2 or x1==x2:
                if y1==y2:
                    if x2<x1:
                        y1,y2=y2,y1
                        x1,x2=x2,x1
                    flag=False
                    for k in range(x1+1,x2):
                        if country[y1][k]:
                            flag=True
                            break
                    if not flag:
                        heappush(bridge,(abs(x1-x2),left,right))
                if x1==x2:
                    if y2<y1:
                        y1,y2=y2,y1
                        x1,x2=x2,x1
                    flag=False
                    for k in range(y1+1,y2):
                        if country[k][x1]:
                            flag=True
                            break
                    if not flag:
                        heappush(bridge,(abs(y1-y2),left,right))


par= list(range(cnt+1))

def find(v):
    if par[v]==v:
        return v
    else:
        par[v]= find(par[v])
        return par[v]

def union(u, v):
    r1= find(u)
    r2= find(v)
    if r1<r2:
        par[r2]=r1
    else:
        par[r1]=r2
ans=0
#print(bridge)
while bridge:
    cost, left, right= heappop(bridge)
    if cost<3:
        continue
    find(left)
    find(right)
    if find(left)!=find(right):
        #print(left,right,cost-1)
        union(left,right)
        ans+=(cost-1)
for i in range(1,cnt+1): # 이거 또 해줘야함?
    find(i)
if par[1:] != [1]*cnt:
    print(-1)
else:
    print(ans)

'''
10 6
0 0 0 1 0 0
0 0 0 1 0 0
0 1 0 0 0 1
0 0 0 0 0 0
1 1 0 1 1 0
1 0 0 0 1 0
1 1 0 0 1 0
0 0 0 0 1 1
0 0 0 0 0 0
0 1 0 0 0 0

13
'''