from bisect import bisect_right as bs
n= int(input())
A= [int(input()) for _ in range(n)]
st= A.index(min(A))
B= A[st:]
m=n-st
dp= [-1e9]+[1e9]*m
for i in range(m):
    spot= bs(dp,B[i])
    dp[spot]= min(dp[spot],B[i])
idx=0

for i in range(m,-1,-1):
    if dp[i]<1e9:
        idx=i
        break
print(dp)
print(idx)
print(n-idx+1)


'''
10 1 5 2 3
0 1 2 3 4
7 8 9 1 2 

반례:
5 6 1 3 2 9 8 10 13
5 1 3 2 6 8 9 10 13
1 3 2 5 6 8 9 10 13
1 2 3 5 6 8 9 10 13



1 2 8 10 13

5 6 3 9

6이 9 전으로 붙었는데 그게 자기 자리임
'''