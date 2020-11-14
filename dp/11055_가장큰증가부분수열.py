#dp[i]: i번째 숫자를 끝으로 한 가장 큰 증가 부분 수열
N = int(input())
A=[0]+[int(i) for i in input().split()]
dp=A[:]
for i in range(1,N+1):
    for j in range(1,i+1):
        if A[i]>A[j]:
            #print(f"A[{i}]>A[{j}]:")
            #print(f'dp[{j}]+A[{i}]={dp[j]}+{A[i]}')
            dp[i] = max(dp[i], dp[j]+A[i])
        #print(dp)

print(max(dp))

'''
10
1 100 2 50 60 3 5 6 7 8
'''