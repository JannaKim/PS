from functools import cmp_to_key as cmp
from random import *
dic={}
data=list(range(26))
shuffle(data)
for i in range(26):
    dic[chr(65+i)]=data[i]
print(dic)

N = int(input())
L=[input() for _ in range(N)]

def Janna(a,b):
    for i in range(min(len(a), len(b))):
        if a[i]!=b[i]:
            return dic[a[i].upper()]-dic[b[i].upper()]
    if len(a)>=len(b):
        return -1
    else:
        return 1

L.sort(key=cmp(Janna))
print(L)

'''
14
but
i
wonti
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
'''