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
    if i>N or i-1+T[i]>N:
        return
        mx=max(mx,accum)
    dfs(i-1+T[i], accum+P[i])
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