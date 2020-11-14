# K 개의 수를 모두 사용했을땐, 가장 큰 숫자로 처음에 N-K개만큼 이으면 된다.
# sort?
from functools import cmp_to_key

K, N = [int(i) for i in input().split()] # K<=N
L=[]
for _ in range(K):
    L.append(int(input()))


def f(a,b):
    #print(a,b)
    state=0
    # 크거나 같고 짧은 쪽이 이김
    mx=0

    for num1, num2 in list(zip(str(a), str(b)))[::-1]: # 큰자리수 하나씩 비교
        mx=max(mx,int(num1))
        if int(num1)>int(num2):
            state=1
        elif int(num1)<int(num2):
            state=-1
        else:
            pass
    if len(str(a))==len(str(b)):
        return state
    if state!=0:
        return state
    else: # state==0
        if len(str(a))>len(str(b)):
            for nm in str(a)[len(str(b)):]:  
            #print(f'nm={nm} mx1={mx2}, state={state}')
                if mx <= int(nm):
                    pass
                else: # b wins
                    return -1
            return 1
        elif len(str(a))<len(str(b)):
        #print(a, b, '!')
            for nm in str(b)[len(str(a)):]:
                #print(f'nm={nm} mx1={mx1}, state={state}')
                if mx <= int(nm):
                    pass
                else: # a wins
                    return 1
            return -1


    
L.sort(key=cmp_to_key(f), reverse=True)

print(L)
M=sorted(L, reverse=True)
print(str(M[0])*(N-K), end='')
print(*L,sep='')

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


2 2
96
991
'''
