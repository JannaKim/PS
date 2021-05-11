# 타 승장 도착 시간, 티켓 등급
from heapq import heappush, heappop
def solution(t, r):
    n= len(t)
    q=[]
    for i in range(n):
        heappush(q,[t[i],r[i],i])
    chk= [False]*(10000+1)
    ans=[]
    while q:
        a, b, c= heappop(q)
        print(a,b,c)
        if chk[a]:
            heappush(q, [a+1,b,c])
        else:
            ans.append(c)
            print(a)
            chk[a]=True

    return ans
print(solution([1,1,0,0], [0,2,2,2]))
#print(solution([7,6,8,1], [0,1,2,3]))