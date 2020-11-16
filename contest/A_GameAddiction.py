from sys import *
# 최단 경로의 개수
H, N = map(int, input().split())
if H==N:
    print(1)
    exit()
start, goal = max(H,N), min(H,N)
mp=[]
for _ in range(start+1):
    mp.append([0]*(start+1))
for i in range(goal,start):
    mp[i][start]=1


for i in range(start-1,goal-1,-1):
    for j in range(i,goal-1,-1):
        mp[j][i]=mp[j+1][i]+mp[j][i+1]
        #[print(i) for i in mp]
        #print()
    

print(mp[goal][goal])