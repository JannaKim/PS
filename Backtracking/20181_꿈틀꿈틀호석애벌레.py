import sys
sys.setrecursionlimit(100005)
N, K = map(int, input().split())
L = [int(i) for i in input().split()]

mx=-1
def dfs(i,accum):
    global mx
    if i>N-1:
        mx=max(mx, accum)
        return
    s=0
    for j in range(i,N):
        s+=L[j]
        if s>=K:
            dfs(j+1, accum+s-K)
            break
    dfs(i+1,accum)


dfs(0,0)

print(mx)
'''
9 6
1 5 4 4 2 3 10 3 5
'''