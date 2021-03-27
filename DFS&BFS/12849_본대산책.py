#MLE 
from collections import deque
d= int(input())
M= int(1e9)+7
'''
정보 전산 미래 신양 한경 진리 학생 형남
0   1   2   3   4   5   6  7
'''

edge= [[] for _ in range(8)]
'''
0 1
0 2
1 2
1 3
2 3
3 4
2 4
3 5
4 5
5 6
6 7
4 7
'''
dist= [0]*9
dist[1],dist[2]=1,1
dist[3],dist[4]=2,2
dist[5],dist[7]=3,3
dist[6]=4

L=[(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (2, 4), (3, 5), (4, 5), (5, 6), (6, 7), (4, 7)]
for a,b in L:
    edge[a].append(b)
    edge[b].append(a)
q=deque()
q.append((0,0))
ans=0
while True:
    v, t= q.popleft()
    if t>=d:
        break
    
    for v2 in edge[v]:
        if v2==0 and t+1==d:
            ans=(ans+1)%M
        if dist[v2]+t+1>d:
            continue
        q.append((v2, t+1))
        #[print(*el) for el in dp]
        #print()
print(ans)




