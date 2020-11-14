# pseudo dijikstra
# idx[엄마 노드] > idx[자식노드]이다: DP문제이다
from time import*
import sys
start = time()
sys.stdin = open('test3.txt', 'r')

N = int(input())
edge = [False] + [[] for _ in range(N)]
dur = [False] + [-1]*N
indegree = [-1]+[0]*N
for i in range(1,N+1):
    L = [int(i) for i in input().split()]
    dur[i] = L[0]
    for j in L[2:]:
        edge[i].append(j) # 간선: i -> 선행(j)될 것
        indegree[j]+=1
# edge = list(set(edge))
#print(edge)
#print(indegree)
accum=[-1] + [0]*N
cnt = 0
def pseudo_dijikstra():
    global cnt
    q=[]
    for i in range(1,N+1):
        if not edge[i]: # i -> ? 간선이 없다면
            accum[i] = dur[i]
    #print(accum)
    for v in range(2,N+1): # 들어오는 v마다 기존의 정보만 갖고도 충분히 완성된다.
        mx=0
        for v2 in edge[v]:
            mx = max(mx, accum[v2])   
            cnt+=1
        accum[v] = dur[v]+mx 
        #print(f'accum[{v}]={accum[v]}')

pseudo_dijikstra()
#print(accum)
print(max(accum[1:]))
print('dp',cnt)
print("time :", time() - start)




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
    

