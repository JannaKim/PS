from functools import cmp_to_key

K, N = [int(i) for i in input().split()] # K<=N
L=[]
for _ in range(K):
    L.append(int(input()))

def f(a,b):
    if int(str(a)+str(b))>=int(str(b)+str(a)):
        return 1
    else:
        return -1



L.sort(key=cmp_to_key(f), reverse=True)

#print(L)
M=[]
for idx, num in enumerate(L):
    M.append((idx,num))
mx = max(M,key=lambda x:x[1])[0]

[print(str(L[i])*((N-K+1) if i==mx else 1),end='') for i in range(len(L))]




'''
3 3
3
2
7

3 4
99
98
99998

99998 99998 99 98
99998 99 9989998

3 4
234
333
1333


4 5
9
12
132
132132913212
'''