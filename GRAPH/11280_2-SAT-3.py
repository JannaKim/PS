import sys; sys.setrecursionlimit(100000)
n, e= map(int, input().split())
edge=[[] for _ in range(2*n)]
for _ in range(e):
    a, b= map(int, input().split())
    if a<0: a = n - a
    if b<0: b= n - b
    a-=1
    b-=1
    edge[(a+n)%(2*n)].append(b)
    edge[(b+n)%(2*n)].append(a)

bundle=[]
b=0
visited=[0]*(2*n) # 정점들에 번호매김
where= [0]*(2*n)
cur=0
q=[]
def scc(v):
    global cur, b
    cur+=1
    visited[v]=cur
    ret= visited[v]
    q.append(v)

    for v2 in edge[v]:
        if not visited[v2]:
            ret= min(ret, scc(v2))
        elif not where[v2]: # 방문은했는데 scc로 안묶임
            ret= min(ret, visited[v2]) # 그중 가장 작은 번호찾기
    
    if ret==visited[v]:
        tmp=[]
        while True:
            ths= q.pop()
            where[ths]=b
            b+=1
            tmp.append(ths)
            if ths==v:
                break
        bundle.append(sorted(tmp))
    return ret

for i in range(2*n):
    if not visited[i]:
        scc(i)

for i in range(n):
    if where[i]==where[n+i]:
        print(0)
        break
else:
    print(1)



'''
import sys
import collections
sys.setrecursionlimit(9990000)

n, m = map(int, sys.stdin.readline().split())

tr = [[] for _ in range(2*n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a<0: a = n - a
    if b<0: b= n - b
    a-=1
    b-=1
    #print(a,b,(a+n)%(2*n),(b+n)%(2*n))
    tr[(a+n)%(2*n)].append(b)
    tr[(b+n)%(2*n)].append(a)


dfsn =[False]*(2*n)
cnt = 1
sn = [-1]*(2*n)
SN = 0
stack = []
finished = [False]*(2*n)
SCC = []

def _scc(cur):
    global cnt, SN
    dfsn[cur] = cnt
    stack.append(cur)
    cnt += 1
    rst = dfsn[cur]
    for nxt in tr[cur]:
        if not dfsn[nxt]:
            rst = min(rst, _scc(nxt))
        else:
            if not finished[nxt]:
                rst = min(rst, dfsn[nxt])
    if rst == dfsn[cur]:
        curSCC = []
        while 1:
            t = stack.pop()
            finished[t] = True
            sn[t] = SN
            curSCC.append(t)
            if t == cur:
                break
        SN+=1
        SCC.append(curSCC)
    return rst

for i in range(2*n):
    if not dfsn[i]:
        _scc(i)

#print(sn)
for i in range(n):
    if sn[i] == sn[n+i]:
        print("0")
        break
else:
    print("1")
'''