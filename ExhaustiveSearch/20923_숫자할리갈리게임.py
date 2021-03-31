# 도도 먼저 시작. 합5 나 5 안나오고 끝나면 수연 승
import sys; input= lambda: sys.stdin.readline().rstrip()
from collections import deque
n, m= map(int, input().split())

dodos_deque=deque()
dodos_ground=[]
suyeons_deque=deque()
suyeons_ground=[]

suyeons_top=-1
dodos_top=-1

for _ in range(n):
    d, s= map(int, input().split())
    dodos_deque.append(d)
    suyeons_deque.append(s)

def bell(deq, first,a, last,b):
    for i in range(a+1):
        deq.appendleft(first[i])
    for i in range(b+1):
        deq.appendleft(last[i])
    

for i in range(m):
    if not i%2: # dodos turn
        ths= dodos_deque.pop()
        if not dodos_deque:
                print('su')
                exit()
        dodos_ground.append(ths)
        dodos_top+=1
        if ths==5:
            bell(dodos_deque, suyeons_ground, suyeons_top, dodos_ground, dodos_top)
            suyeons_ground=[]
            dodos_ground=[]
            dodos_top=-1
            suyeons_top=-1
        if suyeons_top>=0 and ths+suyeons_ground[suyeons_top]==5:
            bell(suyeons_deque, dodos_ground, dodos_top, suyeons_ground, suyeons_top)
            suyeons_ground=[]
            dodos_ground=[]
            suyeons_top, dodos_top= -1, -1
        
    else: # suyeons turn
        ths= suyeons_deque.pop()
        if not suyeons_deque:
            print('do')
            exit()
        
        suyeons_ground.append(ths)
        suyeons_top+=1
        if dodos_top>=0 and ths+dodos_ground[dodos_top]==5:
            bell(suyeons_deque, dodos_ground, dodos_top, suyeons_ground, suyeons_top)
            suyeons_ground=[]
            dodos_ground=[]
            suyeons_top, dodos_top= -1, -1
        elif ths==5:
            bell(dodos_deque, suyeons_ground, suyeons_top, dodos_ground, dodos_top)
            suyeons_ground=[]
            dodos_ground=[]
            dodos_top=-1
            suyeons_top=-1

    #print(dodos_deque, dodos_ground, '||',suyeons_ground, suyeons_deque)

Su= len(suyeons_deque)
Do= len(dodos_deque)

if Su==Do:
    print('dosu')
elif Su>Do:
    print('su')
else:
    print('do')


'''
1,2 WA: 플레이어 덱 앞에다 그라운드 이어야 했다. 잘못 이음
3,4 RE: = +
5 TLE: deque이용 안했다
'''