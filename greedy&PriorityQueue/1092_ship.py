from heapq import heappush, heappop
n= int(input())
crane= [*map(int, input().split())]
crane.sort(reverse=True)
m= int(input())
L=[*map(int, input().split())]

if max(L)>max(crane):
    print(-1)
    exit()
L.sort(reverse=True)

q=[]
for el in L:
    heappush(q,-el) # 무거운거부터

cnt=0
while q:
    cnt+=1
    
    for i in range(n):
        remain=[]
        found=False
        while q:
            wei= heappop(q)
            wei=-wei
            if crane[i]>=wei:
                found=True
                break
            else:
                remain.append(wei)
        for el in remain:
            heappush(q,-el) 
        if not found:
            n=i
print(cnt)


'''
import sys
input = sys.stdin.readline

N = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)
M = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)

time = 0
count = 0

if crane[0] < box[0]: 
    print(-1)
    count = M
    
pos = [0 for _ in range(N)]

while count < M:
    for i in range(N):
        for j in range(pos[i],len(box)):
            if crane[i] >= box[j]:
                count += 1
                pos[i] += 1
                box[j] = float('inf')
                break
            else:
                pos[i] += 1
    time += 1
if time>0: print(time)
    
'''