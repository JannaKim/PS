from math import log
N = int(input())
L = [int(input()) for _ in range(N)]




def f(num,d):
    return (num//10**d)%10


def radix(L,d):
    B=[-1]*len(L)
    C=[0]*10

    for a in L:
        C[f(a,d)]+=1
    for i in range(9):
        C[i+1]+=C[i]

    for i in range(len(L)-1,-1,-1):
        B[C[f(L[i],d)]-1] = L[i]
        C[f(L[i],d)]-=1
    return B




def radix_sort(L):
    digit = int(log(max(L), 10))
    for d in range(digit+1):
        ans=radix(L,d)
    return ans



[print(i) for i in radix_sort(L)]
# N이 최대 10,000,000인 경우 기본적으로 int형이 24byte(python)기에 240MB 이상이 필요하게 됩니다.
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

# 리스트를 쓰지 않는 것이 아니라, 수의 범위(최대 10000)가 정해져있기에 리스트의 크기를 그에 맞춰서 작성하면 메모리는 문제가 되지 않습니다.
'''

'''
10
5
2
3
1
4
2
3
5
1
7
'''