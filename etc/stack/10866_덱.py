from collections import deque
from sys import *; input = lambda: stdin.readline().rstrip()
N = int(input())
dic={}
dic['push_front']=0
dic['push_back']=1
dic['pop_front']=2
dic['pop_back']=3
dic['size']=4
dic['empty']=5
dic['front']=6
dic['back']=7

def f(Q,idx,num):
    if idx==0:
        Q.appendleft(num)
    elif idx==1:
        Q.append(num)
    elif idx==2:
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif idx==3:
        if Q:
            print(Q.pop())
        else:
            print(-1)
    elif idx==4:
        print(len(Q))
    elif idx==5:
        if Q:
            print(0)
        else:
            print(1)
    elif idx==6:
        if Q:
            q=Q.popleft()
            print(q)
            Q.appendleft(q)
        else:
            print(-1)
    else:
        if Q:
            q=Q.pop()
            print(q)
            Q.append(q)
        else:
            print(-1)
    return
Q=deque()
for _ in range(N):
    *el,=input().split()
    f(Q,dic[el[0]],int(el[1]) if len(el)>1 else 0)

'''
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
'''