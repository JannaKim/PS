# 감소면 최대한으로 꼬여있는 경우이다. 그려보기
n = int(input())
# acs_dp[i]: i를 끝으로 만들 수 있는 최장 증가수열
# 답: n-max(asc_dp)
w=[]
for _ in range(n):
    w.append([int(i) for i in input().split()])

w.sort(key = lambda x:x[1])
wire= [i[0] for i in w]
acs_dp=[]
for i in range(n):
    acs_dp.append(1)
    for j in range(i):
        if wire[j]<wire[i] and acs_dp[i]<acs_dp[j]+1:
            acs_dp[i]=acs_dp[j]+1
'''            
des_dp=[]
for i in range(n):
    des_dp.append(1)
    for j in range(i):
        if wire[j]>wire[i] and des_dp[i]<des_dp[j]+1:
            des_dp[i]=des_dp[j]+1
'''
print(n-max(acs_dp))
'''
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6

'''
# https://www.acmicpc.net/problem/2565