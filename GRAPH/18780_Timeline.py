import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
n, m, c= map(int, input().split())
date= [*map(int, input().split())]
edge= [[] for _ in range(n+1)]
indegree= [0]*n
for _ in range(c):
    a, b, s= [int(i)-1 for i in input().split()]
    s+=1
    edge[a].append((b,s))
    indegree[b]+=1

def cal(v):
    for v2, s2 in edge[v]:
        indegree[v2]-=1
        date[v2]= max(date[v2],date[v]+s2)
        if indegree[v2]==0:
            cal(v2)
starts=[]
for i in range(n):
    if indegree[i]==0:
        starts.append(i)

for v in starts:
    cal(v)

[print(date[i]) for i in range(n)]