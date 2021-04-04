n, k= map(int, input().split())
from collections import deque
#3 4 5 6 7 8 9 10 11 
sz=int(max(n+1, k+1)+(1.5))
chk= [False]*sz

q=deque()
q.append((n,0))

while q:
    loc, t= q.popleft()
    if loc==k:
        print(t)
        break
    jump= loc*2
    if jump<sz and not chk[jump]:
        chk[jump]=True
        q.append((jump, t+1))
    if loc+1<sz and not chk[loc+1]:
        chk[loc+1]=True
        q.append((loc+1, t+1))
    if loc-1>=0 and not chk[loc-1]:
        chk[loc-1]=True
        q.append((loc-1, t+1))

'''
a 2*a
'''