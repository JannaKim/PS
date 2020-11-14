# pseudo dijikstra
# 시간 초과
# indegree와 비교했을 때 시간 10배 차이난다. 왜?
# 바른 정보가 아직 도착하지 않았을 때,
# 바르지 않은 정보인 경우에도 계속 전달을 한다.
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
        edge[j].append(i) # 간선: 선행(j) -> i
        indegree[i]+=1
# edge = list(set(edge))
#print(edge)
#print(indegree)
accum=[-1] + [0]*N
cnt = 0
def pseudo_dijikstra():
    global cnt
    q=[]
    for i in range(1,N+1):
        if indegree[i]==0:
            accum[i] = dur[i]
            q.append((accum[i],i))
    while q:
        tmp, v = q.pop(0)
        if accum[v]>tmp:
            continue
        for v2 in edge[v]:
            if tmp+dur[v2]>accum[v2]:
                accum[v2] = tmp+dur[v2]
                cnt+=1
                q.append((accum[v2], v2))

pseudo_dijikstra()
#print(accum)
print(max(accum[1:]))
print('pseudo dijik',cnt)
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
    

