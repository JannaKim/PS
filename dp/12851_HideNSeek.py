from heapq import heappop, heappush
n, k= map(int, input().split())
mn=abs(n-k)
way=1
M= 200000
dp= [1e9]*(M+1)



q= []
heappush(q, (0, k))
mn= 1e9
ans=0
while q:
    cnt, stair = heappop(q)
    if stair ==n and cnt<=mn:
        if cnt<mn:
            ans=1
        else:
            ans+=1
        mn=cnt
        continue
    if stair==M:
        continue
    if dp[stair]<cnt:
        continue
    if not stair%2 and cnt+1<=dp[stair//2]:
            dp[stair//2]= cnt+1
            heappush(q, (cnt+1,stair//2))
    if cnt+1<=dp[stair+1]:
        dp[stair+1]= cnt+1
        heappush(q, (cnt+1,stair+1))
    if stair==0:
        continue
    if cnt+1<=dp[stair-1]:
        dp[stair-1]= cnt+1
        heappush(q, (cnt+1,stair-1))

print(mn, ans,sep='\n')
