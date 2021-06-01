n= int(input())
from collections import deque
st, ed = map(int, input().split())
m= int(input())
edge= [[] for _ in range(n+1)]
for _ in range(m):
    a, b= map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

chk =[False]*(n+1)
chk[st]=True

q=deque()
q.append((st,0))
while q: #
    v, floor= q.popleft()
    if v==ed:
        print(floor)
        exit()
    for v2 in edge[v]:
        if not chk[v2]:
            chk[v2]=True
            q.append((v2,floor+1))
print(-1) # 친척관계가 전혀 없어서..

#1: dfs 써서 틀림
#2: -1 인경우 생각 안해서 틀림