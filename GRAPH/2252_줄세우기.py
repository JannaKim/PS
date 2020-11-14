N, M = [int(i) for i in input().split()] # N: 꼭짓점 개수 M:변의 개수
S=[]
[S.append([]) for _ in range (N+1)]
for _ in range(M):
    a, b = [int(i) for i in input().split()]
    S[a].append(b) # 변의 방향 a->b
#print(S)

chk=[False]*(N+1)
Q=[]

def f(id):

    chk[id]=True
    
    for i in S[id]: # 꼭짓점 i가 가진 변마다 돌림
        if chk[i]==False:
            f(i)
    Q.insert(0,id) # 스택에 함수호출이 종료되는 순서대로 쌓아준다
    #print(Q)

for edges in range(1,N+1):
    if chk[edges]==False:
            f(edges)
#print(f'\ncycle = {cycle}')
print(*Q)

# 75%에서 틀림   ??

'''
3 2
1 3
2 3

7 8
1 2
1 3
1 4
2 5
5 7
3 6
3 5
6 2

8 9
1 3
1 8
1 4
3 2
3 6
8 2
6 8
2 5
5 7



10 1
1 2
'''
