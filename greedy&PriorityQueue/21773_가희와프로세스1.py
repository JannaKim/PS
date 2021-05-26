from heapq import heappop, heappush
t, n= map(int, input().split())
sch=[]
for _ in range(n):  
    id, et, rank= map(int, input().split())
    heappush(sch, (-rank,id,et))

for _ in range(t):
    if not sch:
        break
    r, id, et= heappop(sch)
    print(id)
    if et-1:
        heappush(sch, (r+1,id,et-1))