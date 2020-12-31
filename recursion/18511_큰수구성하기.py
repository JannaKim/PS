from sys import *

N, K = map(int, input().split())
L = [int(i) for i in input().split()]
L.sort(reverse=True)

lenN=len(str(N))
S = ['-']*lenN

def rec(digit,S,end):
    if digit==end: 
        num= int("".join(S));
        if num<=N: 
            print(num)
            exit()
    else:
        for el in L:
            tempS= S[:]
            tempS[digit]=str(el)
            rec(digit+1,tempS,end)

rec(0,S,lenN)
rec(0,['-']*(lenN-1),lenN-1) # 작은 자리수일때.


'''
657 3
1 5 7
'''