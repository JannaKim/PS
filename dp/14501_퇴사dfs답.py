from sys import *; input= lambda: stdin.readline().rstrip()

N = int(input())
T, P= [0], [0]
for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)
ans= 0
def dfs(day, profit):
    global ans
    if day ==N+1:
        ans= max(ans, profit)
        return
    elif day>N+1:
        return
    dfs(day+T[day], profit+P[day])
    dfs(day+1,profit)

dfs(1,0)
print(ans)



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