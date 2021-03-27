#TLE: sys 안해줘서
import sys; input= lambda: sys.stdin.readline().rstrip()

n, m, v= map(int, input().split())
v-=1
L= [*map(int, input().split())]
cl= n-v
for _ in range(m):
    ques= int(input())
    if ques<n:
        print(L[ques])
    else:
        ques-=v
        print(L[v+ques%cl])


# version 2
'''
import sys; input= lambda: sys.stdin.readline().rstrip()
n, m, v= map(int, input().split())
v-=1
L= [*map(int, input().split())]
cycle= L[v:][:]
cl= len(cycle)
for _ in range(m):
    ques= int(input())
    if ques<n:
        print(L[ques])
    else:
        ques-=n
        print(cycle[ques%cl])

'''