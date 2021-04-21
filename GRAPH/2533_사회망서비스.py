import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000000)
n= int(input())
edge= [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v= map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

'''
d=0
start=0
def travel(v,v1,depth):
    flag=False
    for v2 in edge[v]:
        if v1==v2:
            continue
        flag=True
        travel(v2,v,depth+1)
    if not flag:
        global d,start
        if d<depth:
            d=depth
            start=v
travel(1,0,0)
'''
def dfs(v,v1,switch):
    tmp=0
    if switch:
        tmp+=1
    for v2 in edge[v]:
        if v1==v2:
            continue
        tmp+=dfs(v2,v,not switch)
    return tmp
#print(start)
ox= dfs(1,0,True)


print(min(ox,n-ox))