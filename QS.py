'''
from random import*
data = list(range(1,11))
shuffle(data)
print(data)
'''
N = int(input())
data = [int(input()) for _ in range(N)]
def QS(L,first,last):

    if first>=last:
        return []
    p = L[first]
    A = []
    B = []
    M = [p]
    for i in range(first+1,last+1):
        if L[i]<p:
            A.append(L[i])
        elif L[i]>p:
            B.append(L[i])
        else:
            M.append(L[i])

    for idx, i in enumerate(range(first,first+len(A))):
        L[i] = A[idx]
    for idx, i in enumerate(range(first+len(A),first+len(A)+len(M))):
        L[i] = M[idx]
    for idx, i in enumerate(range(first+len(A)+len(M),last+1)):
        L[i] = B[idx]
        
    QS(L,first,first+len(A)-1) # first부터 len(A)개: first, first+len(A)+1 7부터 5개: 7+5-1
    QS(L, first+len(A)+len(M), last) # 앞에꺼 이상부터

QS(data,0,N-1)
[print(i) for i in data]
        
'''
import sys
input = sys.stdin.readline
n = int(input())
cnt = [0 for i in range(10000+1)]
for i in range(n):
    cnt[int(input())] += 1
for i in range(1, 10000+1):
    for j in range(cnt[i]):
        print(i)
'''