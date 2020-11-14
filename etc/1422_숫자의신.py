# K 개의 수를 모두 사용했을땐, 가장 큰 숫자로 처음에 N-K개만큼 이으면 된다.
# sort?
from functools import cmp_to_key

K, N = [int(i) for i in input().split()] # K<=N
L=[]
for _ in range(K):
    L.append(int(input()))


def f(a,b):
    #print(a,b)
    mx1=0
    mx2=0
    state=0
    # 크거나 같고 짧은 쪽이 이김
    for num1, num2 in zip(str(a), str(b)): # 큰자리수 하나씩 비교
        mx1=max(mx1,int(num1))
        mx2=max(mx2,int(num2))
        if int(num1)>int(num2):
            state=1
        elif int(num1)<int(num2):
            state=-1
        else:
            pass
    #print(f'a={a}, len(str(a))={len(str(a))}, b = {b}, len(str(b))={len(str(b))}')
    if len(str(a))==len(str(b)): # 자릿수가 같을때
        return state
    # 자릿수가 큰 애의 나머지숫자들이 
    # 짧은 애의 제일 큰 숫자보다 모두 크면 긴 애가 이김
    elif len(str(a))>len(str(b)):
        #print(a, b, '!!')
        for nm in str(a)[::-1][len(str(b)):]:  
            #print(f'nm={nm} mx1={mx2}, state={state}')
            if mx2 <= int(nm):
                pass
            else: # b wins
                return -1
        return 1

    elif len(str(a))<len(str(b)):
        #print(a, b, '!')
        for nm in str(b)[::-1][len(str(a)):]:
            #print(f'nm={nm} mx1={mx1}, state={state}')
            if mx1 <= int(nm):
                pass
            else: # a wins
                return 1
        return -1

'''
        if state==1 or state==0:
            return 1 # a wins
        else:
            return -1
'''
'''
        if state==-1 or state==0:
            return -1 # b wins
        else:
            return 1
            '''
 


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

'''
