# 시간초과
from functools import cmp_to_key as cmp
N, C = map(int, input().split())
dic={}
*L, = map(int, input().split())

dic = {}



for el in L:
    if el not in dic:
        dic[el]=1
    else:
        dic[el]+=1

M=[]
for k , v in dic.items():
    M.append((k,v))

#print(M)




def f(a,b):
    if a[1]!=b[1]:
        return a[1]-b[1]
    else:
        return L.index(b[0])-L.index(a[0])





M.sort(key=cmp(f)) # N^2logN

[print((str(a)+' ')*b, end='') for a,b in M[::-1]]







'''
for idx in range(N,0,-1):
    if not CNT[idx]:
        continue
    elif len(CNT[idx])==1:
        [ans.append(*CNT[idx]) for _ in range(idx)]
    else:
        CNT[idx].sort(key = lambda x: L.index(x))
        for el in CNT[idx]:
            [ans.append(el) for _ in range(idx)]
print(*ans)
'''
'''
6 2
2 2 2 1 1 1

5 2
2 1 2 1 2
'''




