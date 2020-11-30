#해결 i날 전까지 끝낸 i 가져가서
from sys import *; input= lambda: stdin.readline().rstrip()

N = int(input())
T, P= [0], [0]
for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

mx=0
def dfs(i,accum):
    global mx
    if i>N+1:
        return
    mx=max(mx,accum)
    if i==N+1:
        return
    dfs(i+T[i], accum+P[i])
    dfs(i+1,accum)

dfs(1,0)
print(mx)

'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''