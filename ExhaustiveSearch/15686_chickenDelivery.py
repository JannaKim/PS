n, m= map(int, input().split())

road= [[-1]*(n+1)]
road+= [[-1]+[*map(int,input().split())] + [-1] for _ in range(n)]
road+= [[-1]*(n+1)]

homes= []
nB=0
h=0
for i in range(1, n+1):
    for j in range(1,n+1):
        if road[i][j]==1:
            h+=1
            homes.append((i,j))
        elif road[i][j]==2:
            nB+=1

branchbyHome=[[0]*h for _ in range(nB)]
cur=0
for i in range(1, n+1):
    for j in range(1,n+1):
        if road[i][j]==2:
            sm=0
            for idx, (a, b) in enumerate(homes):
                branchbyHome[cur][idx]= abs(i-a)+abs(j-b)
            cur+=1

chk=[False]*nB

def count():
    sum=0
    for i in range(h):
        mn=1e9
        for j in range(nB):
            if chk[j]:
                mn= min(mn, branchbyHome[j][i])
        sum+=mn
    return sum


def chooseBranch(i,cnt):
    if cnt==m:
        return count()
    if i==nB:
        return 1e9
    chk[i]=True
    mini=1e9
    mini= min(mini, chooseBranch(i+1,cnt+1))
    chk[i]=False
    mini= min(mini,chooseBranch(i+1,cnt))

    return mini

print(chooseBranch(0,0))
