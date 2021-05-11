from heapq import heappop, heappush
t= int(input())
for _ in range(t):
    n= int(input())
    microwave= [*map(int, input().split())]
    eat= [*map(int, input().split())]
    q=[]
    for i in range(n):
        heappush(q, (-microwave[i], eat[i]))
    res=0
    ans=0
    while q:
        w, e= heappop(q)
        res-=w
        ans= max(ans, res+e)
    print(ans)