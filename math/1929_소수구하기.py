from math import *
N, M = map(int, input().split())
L = [False, False, True, True]+ [True]*M
for i in range(2,M//2+1):
    for j in range(2*i,M+1,i):
        
        L[j]=False

for i in range(N,M+1):
    if L[i]==True: print(i)


#소수는 1이 아닌 자연수 중에서 1과 자기 자신 이외의 약수를 갖지 않는 수입니다. 