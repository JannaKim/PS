T = int(input())
for _ in range(T):
    n = int(input())
    L = [int(i) for i in input().split()]
    
    edge = [False]+[[] for _ in range(n)]
    rv_edge = [False]+[[] for _ in range(n)]

    indegree=[-1]+[0]*n

    for i in range(len(L)-1): # 0~n-1 (n개)
        for j in range(len(L)-1,i,-1): # n + n-1 + ... 2 + 1: 두 정점을 잇는 가짓수
            edge[L[i]].append(L[j])
            # L5CA?
            indegree[L[j]]+=1


    '''
    for a, b in zip(L, L[1:]):
        edge[a].append(b)
        indegree[b]+=1
        rv_edge[b].append(a)
    '''
    m = int(input())
    if m==0:
        print(*L)
        continue
    for _ in range(m):
        a, b = map(int, input().split())
        # 떨어져있을 때
        if L.index(a)<L.index(b): # a->b 를 b->a로
            edge[a].remove(b)
            indegree[b]-=1
            edge[b].append(a)
            indegree[a]+=1
        else:
            edge[b].remove(a)
            indegree[a]-=1
            edge[a].append(b)
            indegree[b]+=1

    stack=[]

    print(edge)
    print(indegree)
    q = [i for i in range(1,n+1) if indegree[i]==0]
    print('q',q)
    if len(q)>1: # 주종관계불확실
        print('?')
        continue
    if not len(q):
        print('IMPOSSIBLE')
        continue

    while q:
            v = q.pop(0)
            stack.append(v)
            for v2 in edge[v]:
                indegree[v2]-=1
                if indegree[v2]==0:
                    q.append(v2)

    # cycle이 있다면 impossible
    # 정보가 부족하다면
    if len(stack)!=len(L):
        print('IMPOSSIBLE')
    else:
        print(*stack)


'''
행렬로 
N*M 일때 
a->b이면
바뀌는거 많음, 완전그래프
간선개수가 v^2과 비슷
완전그래프일때 행렬해보기
'''

'''
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3

1
5
5 4 3 2 1
2
2 4
3 4
'''


'''
        if b not in edge[a] and a not in edge[b]: # 누가 위에 있는지 알아내야함..
            edge[a].append(b)
            rv_edge[b].append(a)
            indegree[b]+=1
        else:
            if a in edge[b]: # b->a 를 a->b로
                if a==3 and b==4:
                    print('a,b=',a,b)
                # rv_edge renew 해줘야함
                edge[b].remove(a)
                rv_edge[a].remove(b)
                indegree[a]-=1
                L = edge[a][:]
                M = rv_edge[b][:]
                for v1 in M:
                    edge[v1].remove(b)
                    rv_edge[b].remove(v1)
                    indegree[b]-=1

                    edge[v1].append(a)
                    rv_edge[a].append(v1)
                    indegree[a]+=1

                    if a==3 and b==4:
                        print(f'edge[{v1}]={edge[v1]}')
                

                for v2 in L:
                    edge[b].append(v2)
                    rv_edge[v2].append(b)
                    indegree[v2]+=1

                    edge[a].remove(v2)
                    rv_edge[v2].remove(a)
                    indegree[v2]-=1
                
                
                edge[a].append(b)
                rv_edge[b].append(a)
                indegree[b]+=1

            if b in edge[a]: # a->b 를 b->a
                edge[a].remove(b)
                indegree[b]-=1
                L = edge[b][:]
                M = rv_edge[a][:]
                for v1 in M:
                    edge[v1].remove(a)
                    rv_edge[a].remove(v1)
                    indegree[a]-=1

                    edge[v1].append(b)
                    rv_edge[b].append(v1)
                    indegree[b]+=1
                for v2 in L:
                    edge[a].append(v2)
                    rv_edge[v2].append(a)
                    indegree[v2]+=1

                    edge[b].remove(v2)
                    rv_edge[v2].remove(b)
                    indegree[v2]-=1

                
                edge[b].append(a)
                rv_edge[a].append(b)
                indegree[a]+=1
'''