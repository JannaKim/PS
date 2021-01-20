from heapq import heappush, heappop

# ['', '', 'heappush(q, el)', 'heappop(q)']

# 1->n, must pass ? ? .. a-> bc ->d
n, e= map(int, input().split())

edge= [[] for _ in range(n+1)]

for _ in range(e): 
    a, b, c= map(int, input().split())
    edge[a].append((b, c))
    edge[b].append((a, c))


frst, scnd= map(int, input().split())
# a ->
# b ->
# c ->

# E+ vlogv fib heap? O(logn)?
a= [1e9]*(n+1) #####################

b= [1e9]*(n+1)

C= [1e9]*(n+1)


q=[]

# a ->
heappush(q, (0, 1))
a[1]=0
while q:
    c, v= heappop(q)

    if a[v]<c:
        continue

    for v2 in edge[v]:
        cost= c+ v2[1]
        if a[v2[0]]<=cost: continue
        else: 
            a[v2[0]]= cost
            heappush(q, (cost, v2[0]))
    

# b ->
heappush(q, (0, frst))
b[frst]=0
while q:
    c, v= heappop(q)

    if b[v]<c:
        continue

    for v2 in edge[v]:
        cost= c+ v2[1]
        if b[v2[0]]<=cost: continue
        else:
            b[v2[0]]= cost  ###################
            heappush(q, (cost, v2[0])) ####################

# C ->

heappush(q, (0, scnd)) # own #########################
C[scnd]=0
while q:
    c, v= heappop(q)

    if C[v]<c:
        continue

    for v2 in edge[v]:
        cost= c+ v2[1]
        if C[v2[0]]<=cost: continue
        else:
            C[v2[0]]= cost 
            heappush(q, (cost, v2[0]))



# a -> b+ b ->c + c->d
# a ->c + c->b + b ->d min

# frst, scnd
ans= min(a[frst] + b[scnd] + C[n], a[scnd]+ C[frst]+ b[n])

if ans>=1e9: print(-1)
else: print(ans)
    
'''
https://www.acmicpc.net/problem/10217
'''