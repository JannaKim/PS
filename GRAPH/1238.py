from heapq import heappush as push, heappop as pop
N, M, X = map(int,input().split())
edge = [[] for _ in range(N+1)]
edge2= [[] for _ in range(N+1)]
# node -> X, X-> nodes 두번 쓰기

for _ in range(M):
    a, b, T = map(int,input().split())
    edge[b].append((T,a)) # X->node
    edge2[a].append((T,b))

total_time = [100*N]*(N+1)
def heapq():
    global total_time
    q=[]
    push(q,(0,X))
    total_time[X]=0
    while q:
        T, to = pop(q)
        #print('현재 node',to)
        if T> total_time[to]:
            continue
        for time, nxt in edge[to]:
            if T + time < total_time[nxt]:
                total_time[nxt] = T+time
                push(q,(total_time[nxt], nxt))

total_time2 = [100*N]*(N+1)
def heapq2():
    global total_time2
    q=[]
    push(q,(0,X)) # X에서 시작
    total_time2[X]=0
    while q:
        T, to = pop(q)
        #print('현재 node',to)
        if T> total_time2[to]:
            continue
        for time, nxt in edge2[to]:
            if T + time < total_time2[nxt]:
                total_time2[nxt] = T+time
                push(q,(total_time2[nxt], nxt))

heapq()
#print(total_time[1:])

heapq2()
#print(total_time2[1:])

ans=[]
for a, b in zip(total_time[1:],total_time2[1:]):
    ans.append(a+b)

print(max(ans))
# total_time: 시작->X 가는 최단시간

'''
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''