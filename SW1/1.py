from functools import cmp_to_key as cmp
dic= {}
L= input().split()
n=len(L)
dic={} # 스킬이름을 노드번호로
name=['']*len(L) # 노드번호를 스킬이름으로
for idx, el in enumerate(L):
    dic[el]=idx
    name[idx]=el

# 65~122
e= int(input())

edge=[[] for _ in range(n)] # 소문자 대문자
indegree= [0]*n # 위상
for idx, _ in enumerate(range(e)): # 스킬을 아스키값으로 받는다.
    a, b= input().split()
    edge[dic[a]].append((dic[b],idx)) # idx를 가중치로 받아서 인풋 순서대로 돌리도록함
    indegree[dic[b]]+=1

chk=[False]*(n+1)

q=[]
def topo(v,cnt):
    global chk
    
    edge[v].sort(key= cmp(lambda a, b: a[1]-b[1])) # 간선받는 순서대로
    if not edge[v]:
        if len(q)>1:
            [print(name[el],end=' ') for el in q]
            print() 
    for v2, wei in edge[v]:
        if not chk[v2]:
            q.append(v2)
            chk[v2]=True
            topo(v2,cnt+1)
            q.pop()

start=[]
for i in range(n):
    if indegree[i]==0:
        if edge[i]: # 개인스킬 아닌애들만
            start.append((i,edge[i][0])) # 가중치 제일작은거 하나 같이 넣음

if len(start)>1:
    start.sort(key=lambda a,b: a[1]-b[1])# 가중치 적은순으로 sort

q=[]
for node, wei in start:
    q=[] # 이거 안적었다..  큐 안비워줬다.. 망함 ㅠㅠ
    q.append(node)
    topo(node,1)
        