# DFS Spanning Tree 대표 문제
k = int(input())
nm_v = k+1
edge = [False] + [[] for _ in range(nm_v)]
signs = input().split()
a, b = 1,2
indegree = [-1]+[0]*(nm_v)
for i in range(1,k+1):
    if signs[i-1] == '>': # a<-b
        edge[b].append(a)
        indegree[a]+=1
    else: # a->b
        edge[a].append(b)
        indegree[b]+=1
    a, b = b, b+1
stack=[]
visited = [True] + [False]*(nm_v)
def indegree_BFS(v):

    visited[v]=True
    for v2 in edge[v]:
        if visited[v2]==False:
            indegree_BFS(v2)
    stack.append(v)

def min_indegree_BFS(v):

    visited[v]=True
    for v2 in edge[v][::-1]:
        if visited[v2]==False:
            indegree_BFS(v2)
    stack.append(v)

for i in range(1,nm_v+1):
     if indegree[i]==0:
         indegree_BFS(i)
#print(stack)
mx_order=[[] for _ in range(nm_v+1)]
for idx, i in enumerate(stack):
    mx_order[i] = 9-idx


visited = [True] + [False]*(nm_v)
stack=[]
for i in range(nm_v,0,-1):
     if indegree[i]==0:
        min_indegree_BFS(i)
#print(stack)
mn_order=[[] for _ in range(nm_v+1)]
for idx, i in enumerate(stack):
    mn_order[i] = k-idx

print(*mx_order[1:],sep='')
print(*mn_order[1:],sep='')


'''
8
> > < > > < > <

2
< >
'''
