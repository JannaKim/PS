X = int(input())
a=2
while True:
    if ((a-2)*(a-1))//2<X and X<=((a-1)*a)//2:
        break
    a+=1
# a-1층에 있다
if (a-1)%2: # 홀수라면 정방향
    print(a-(a-1-(((a-1)*a)//2-X)),'/',a-1-(((a-1)*a)//2-X),sep='')
else: 
    print(a-1-(((a-1)*a)//2-X),'/',a-(a-1-(((a-1)*a)//2-X)),sep='')


# i j : 1,1 에서 i,j 까지 가는 경로의 개수
# dp[1][1]=1
'''
if dp[i][j-1]>dp[i][j]: # 좌
    dp[i][j]+=dp[i][j-1]
if dp[i-1][j]>dp[i][j]: # 아래
    dp[i][j]+=dp[i-1][j]

f(a,b):  f(1,1) 에서 f(a,b)까지 가는 경로의 개수
f(a,b) = 
if dp[i][j-1]>dp[i][j]:
    dp[i][j]+=dp[i][j-1]
if dp[i-1][j]>dp[i][j]:
    dp[i][j]+=dp[i-1][j]
'''