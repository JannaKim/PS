import sys; input= lambda: sys.stdin.readline().rstrip()
from collections import deque
n= int(input())

q= [deque() for _ in range(n)]

for i in range(n):
    for el in input().split():
        q[i].append(el)

for el in input().split():
    #print(el)
    flag=False
    for i in range(n):
        if not q[i]:
            continue
        if q[i][0]==el:
            flag=True
            q[i].popleft()
    if not flag:
        print('Impossible')
        exit()
for i in range(n):
    if q[i]:
        print('Impossible')
        exit()
print('Possible')


'''
자신이 기억하고 있는 문장을 끝까지 말한 다음 pps789에게 돌아가며, cseteram은 모든 앵무새가 돌아갈 때 까지 단어를 받아적는다.
'''