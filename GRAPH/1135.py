from functools import cmp_to_key as cmp
n= int(input())
L= [*map(int, input().split())]
edge= [[] for _ in range(n)]
for i in range(n):
    if L[i]<0:
        continue
    edge[L[i]].append(i)


cnt=[0]*n
def f(a,b):
    return cnt[a]-cnt[b]


def dfs2(v,l):
    l+=1
    for v2 in edge[v]:
        return max(l,dfs2(v2,l))
    return l
    

def f(a,b):
    return cnt[a]-cnt[b]
ans=0

def f2(a,b):
    return accum[a]-accum[b]
def dfs3(v,t):
    global ans
    ans=max(ans,t)

    edge[v].sort(key= cmp(f2), reverse=True)

    for v2 in edge[v]:
        t+=1
        dfs3(v2, t)


def dfs(v, t):
    #print(v,t)
    mx= t
    for v2 in edge[v]:
        cnt[v2]= dfs2(v2,0)

    edge[v].sort(key= cmp(f), reverse=True)

    for v2 in edge[v]:
        t+=1
        mx= max(dfs(v2, t),mx)
    return mx

accum= [0]*n
for i in range(n):
    accum[i]= dfs(i,0)

dfs3(0,0)
#print(cnt)
print(ans)


'''
13
-1 0 0 1 2 3 4 2 7 5 7 9 10
\
'''
