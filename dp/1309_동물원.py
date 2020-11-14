# https://www.acmicpc.net/problem/1309
# dp[i][p]: 세로로 i칸일 때 사자를 배치하는 경우의 수
# dp[i][0]: 전 꺼 안채움, dp[i][1]: 왼 쪽, dp[i][0]: 오른쪽

N = int(input())
a= b= c= 1
if N==1:
    print(a+b+c)
else:
    for i in range(2,N+1):
        a, b, c= a+b+c, a+c, a+b
        
    print((a+b+c)%9901) 
