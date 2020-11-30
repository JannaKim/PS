N=int(input())
T=[0]*(N+1)
P=[0]*(N+1)
for i in range(1,N+1):
    T[i], P[i] = map(int, input().split())

mx=-1
def dfs(i,accum):
    global mx
    if i==N+1:
        mx=max(mx,accum)   
        return
    elif i>N+1:
        return
    dfs(i+T[i], accum+P[i])
    dfs(i+1, accum)
    return
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