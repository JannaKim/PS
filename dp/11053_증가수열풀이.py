N = int(input())
L = [int(i) for i in input().split()]
'''
10 20 10 30 20
[[10],[10,20],[10],[10,20,30],[10,20]]
모든 seq를 저장할 필요가 없다.
seq 끝들이 L[i] 라는건 정해짐
그전의 정보를 정의할 수 있는 법?

seq[i]: L[i]가 붙여질 수 있을때 붙임 당하는 seq[]의 인덱스
'''
#

dp = [1] * N # dp[i] : 1~i 번째 중 i번째에서 끝나는 최장 부분 증가수열의 길이
seq=[] # seq[i]: L[i]로 끝나는 최장 증가수열
for i in range(N):
    seq.append(i)
    for j in range(i):
        if L[i] > L[j] and dp[i] < dp[j] + 1: # L[i]=30 일 때, 10 30 도 되고 10 20 30 도 되면 max저장
            dp[i] = dp[j] + 1
            seq[i] = j

# [0, 0, 2, 1, 0, 3]     

a = dp.index(max(dp))   
while True:
    print(L[a],end=' ')
    if a==seq[a]:
        break
    a=seq[a]
    
    
        
    



#print(seq)
#print(max(dp)) # 정답은 모든 dp의 최대값