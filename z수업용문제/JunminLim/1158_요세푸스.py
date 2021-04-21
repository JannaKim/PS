import sys; input= lambda: sys.stdin.readline().rstrip()
a,b=map(int, input().split())
from collections import deque
p=deque()

for i in range (a):
    p.append(i+1)
#순서는 b-1번째

ans=[]
while p:
    for _ in range (b-1):
        tmp= p.popleft()
        p.append(tmp)

    ans.append(p.popleft())


print('<',end='')
for idx, el in enumerate(ans):
    if idx==a-1:
        print(el,end='')
    else:
        print(el,end=', ')
print('>',end='')
   
#print('<'+', '.join(ans)+'>')
