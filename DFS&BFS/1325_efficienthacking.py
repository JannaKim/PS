import sys; 
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
#indegree = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    edge[b].append(a)
    #indegree[a]+=1

#check = [False]*(N+1) # uninitialize visited array?
def dfs(v):
    check = [False]*(N+1)
    check[v]=True
    cnt = 1
    q = deque()
    q.append(v)
    while q:
        v1 = q.popleft()
        for v2 in edge[v1]:
            if not check[v2]:
                cnt+=1
                check[v2]=True
                q.append(v2)
    return cnt



ans=[]
mx=0

for i in range(1,N+1):
    #if not indegree[i]:
    if edge[i]:
        cnt = dfs(i)
        '''
        mx = max(mx, cnt)
        ans.append((i, cnt)) #메모리 초과
        '''
        if cnt>mx: # 새로운 mx찾으면 답 리스트 초기화
            ans=[i]
            mx=cnt
        elif cnt==mx: # 새로운 mx와 같은 애면 리스트 추가
            ans.append(i)
'''       
A = []
[A.append(str(el[0])) for el in ans if el[1]==mx]
print(" ".join(A))
'''

print(*ans)
        


'''
5 4
3 1
3 2
4 3
5 3
'''