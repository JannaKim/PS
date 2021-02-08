from collections import deque
n= int(input())
edge= [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b= map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

chk= [False]*(n+1)
chk[1]=True
q= deque()
q.append(1)
cnt=-1
while q:
    cnt+=1
    v= q.popleft()
    chk[v]=True
    for v2 in edge[v]:
        if not chk[v2]:
            chk[v2]=True
            q.append(v2)
print(cnt)