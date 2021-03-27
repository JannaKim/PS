n= int(input())

chk= [False]*n
def backtrack(k):
    if len(q)==n:
        print(*q)
        return
    for i in range(n):
        if not chk[i]:
            chk[i]=True
            q.append(i+1)
            backtrack(i+1)
            q.pop()
            chk[i]=False
q=[]
backtrack(0)

'''
import sys
input=sys.stdin.readline
n = int(input())
ans = []
visited = [0] * n

def dfs(d):
    if d==n:
        ans.append([num for num in visited])
    else:
        for i in range(n):
            if i+1 in visited: continue
            visited[d] = i+1
            dfs(d+1)
            visited[d] = 0

dfs(0)
for a in ans:
    print(*a)
'''