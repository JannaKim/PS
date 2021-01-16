n= int(input())

while(True):
    seq= 0
    i=0
    while(True):
        next=seq*2+3+i
        if next>=n: 
            break
        seq= seq*2+3+i
        i+=1 
    n-=seq
    if n<=3+i:
        if n==1: print('m'); break;
        else: print('o'); break;
    n-=3+i

###########################################################################

l=lambda n:0 if n<=-1 else 2*l(n-1)+n+3 # 전+지금+전
def f(n,k):
 if n>l(k):return f(n,k+1)
 if n<=l(k-1):return f(n,k-1)
 n-=l(k-1)
 if n<=k+3:return 'm'if n==1 else 'o'
 n-=k+3
 return f(n,k-1)
print(f(int(input()),0))


'''

howMany=0
def moo(n,cnt):
    global howMany
    howMany+=1
    if cnt==0: return'moo'
    side=moo(cnt-1)
    return side+'moo'+'o'*cnt +side


recLen=0

semiAns=moo(n,recLen)
print(semiAns[n-1])
print(howMany)

3
10
25
56
119
246


N = int(input())
totalLen = 0
mLen = 3

while totalLen < N:
    totalLen = (totalLen * 2) + mLen
    mLen += 1

mLen -= 1


def dfs(totalLen, mLen, N):
    splitLen = (totalLen - mLen) // 2

    if N <= splitLen:
        dfs(splitLen, mLen - 1, N)
    elif N > (splitLen + mLen):
        dfs(splitLen, mLen - 1, N - (splitLen + mLen))
    elif splitLen < N <= splitLen + mLen:
        N -= splitLen
        if N == 1:
            print("m")
        else:
            print("o")
        return


dfs(totalLen, mLen, N)

'''
