from heapq import*
import sys; input = lambda: sys.stdin.readline().rstrip(); r = range
n = int(input())
sea=[]
sea.append([-1]*(n+2))
sea += [[-1]+ [*map(int,input().split())]+[-1] for _ in r(n)]
sea.append([-1]*(n+2))
######################################################################################

start = [(y,x) for x in r(1,n+1) for y in r(1,n+1) if sea[y][x] == 9][0]

sea[start[0]][start[1]] = 0

Dx = [0,-1,1,0]
Dy = [-1,0,0,1]

ans = 0
lv = 2
exp = 2
q=[(0, start[0], start[1])]
v=[[False]*(n+2) for _ in r(n+2)]
v[start[0]][start[1]]=True

def dfs(y, x, step):
    





dfs(start[0],start[1])