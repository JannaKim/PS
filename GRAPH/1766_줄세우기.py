from queue import PriorityQueue
N, M = [int(i) for i in input().split()]
edge=[]
[edge.append([]) for _ in range(N+1)]

degree=[-1]+[0]*(N)

for _ in range(M):
    a, b = [int(i) for i in input().split()]
    edge[a].append(b)
    degree[b]+=1


#print(degree)

que = PriorityQueue()

[que.put(i) for i in range(1,N+1) if degree[i]==0]

#print(que.queue)
while que.empty()!=True:
    #print(que.queue)
    a = que.get()
    
    print(a, end=' ')
    
    for i in edge[a]:
        degree[i]-=1
        if degree[i]==0:
            que.put(i)


    
    


'''
4 2
4 2
3 1

12 15
1 2
1 3
1 4
2 3
2 6
3 7
6 5
6 7
2 9
5 8
9 8
7 11
7 10
10 12
9 12
'''
