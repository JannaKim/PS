# i에 걸리는 시간을 구하기 위한 정보가 i이상의 노드에 있을 수 있는 경우

from collections import deque
N = int(input())
edge = [[] for _ in range(N+1)]
dur=[-1]*(N+1)
indegree = [-1]+[0]*N
for i in range(1,N+1):
    *L, = map(int, input().split())
    dur[i]=L[0]
    for el in L[2:]:
        edge[el].append(i)
        indegree[i]+=1

accum = [-1]*(N+1)

Q = deque()
for i in range(1,N+1):
    if indegree[i]==0:
        Q.append(i)
        accum[i]=dur[i]



while Q:
    v = Q.popleft()
    for v2 in edge[v]:
        indegree[v2]-=1
        accum[v2] = max(accum[v2], accum[v]+dur[v2])
        if indegree[v2]==0:
            Q.append(v2)

print(max(accum))

'''
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6
'''


'''

The goal is to collect all infos that affects current vertax(v).
The number of infos related to current v is the num of edge (v0 ->v)
Which means, when v0 has finished to search its max dur(and found it), 
it is then ready to pass over its info to those that need it.

How can I know when a vertax is ready to pass down its info?
It is determined when its indegree is 0

A vertax with indegree 0 means there is no info to collect in order to complete info of itself.

when a vertex with indegree 0 passes down its info to v2,
decrease indegree[v2] once to inform v2 that its amount of effort to search its valid info
has decreased once.

So in this case, list indegree, accum is needed.
list accum  of v2 is renewed each time it receives info(v->v2, such v that its indegree is or has turned to 0 )


In another aspect, 
v can collect its info with accum[v2] when v->v2 
v2 is the info NEEDED to finish v. (make sure to set the heading edge according to it)

but accum[v2] in that instance might not have finshed to renew itself.
How will I know then accum[v2] is ready?
It can be determined by checking indegree[v2]==0
What if indegree[v2]!=0? It means it is of no use to bring accum[v2].

This is why an order of finishing accum[v] should always be placed according to the time line indegree[v] turns 0.
'''