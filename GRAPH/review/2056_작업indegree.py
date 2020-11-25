from time import*
import sys
start = time()
sys.stdin = open('test3.txt', 'r')
N = int(input())
edge = [False]+[[] for _ in range(N)]
dur=[-1]+[0]*N
indegree = [-1]+ [0]*N
for i in range(1,N+1):
    L = [int(i) for i in input().split()]
    dur[i] = L[0]
    for j in L[2:]:
        edge[j].append(i) # 선행 -> 나중
        indegree[i]+=1

accum = [-1] + [0]*N
cnt = 0
def indegree_BFS():
    global cnt
    q = []
    q = [i for i in range(1,N+1) if indegree[i]==0]
    for j in q:
        accum[j] = dur[j]

    while q:
        v = q.pop(0) # 스택에 쌓인것: accum 완성된 것.
        for v2 in edge[v]:
            indegree[v2]-=1
            accum[v2] = max(accum[v2], accum[v]+dur[v2])
            cnt+=1
            if indegree[v2]==0:
                q.append(v2)

indegree_BFS()
print(max(accum[1:]))
print('indegree',cnt)
print("time :", time() - start)

