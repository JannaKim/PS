A = input()
B = input()

# 첫문자열에 하나 추가되면 두번쨰 문자열에 추가돼도
# 첫문자열에서 이만큼 두번째에서 이만큼봤을떄 범위를 보고싶다
# dp[i][j]: 첫번째 문자열1~i 까지 봤을때 두번째에 1~j까지 봤을때 LCS길이
# 어떤 조건에서 LCS길이 1증가할까
# A[i] != B[j] 일때 dp[i][j]= max(dp[i-1][j], dp[i][j-1]): 
# A[i] == B[j]  dp[i][j]= dp[i-1][j-1]+1

dp=[]
for i in range(len(A)+1):
    dp.append([0]*(len(B)+1))



for i in range(len(A)):
    for j in range(len(B)):
        if A[i] != B[j]: 
            dp[i+1][j+1]= max(dp[i][j+1], dp[i+1][j])
        if A[i] == B[j]: 
            dp[i+1][j+1]= dp[i][j] +1

a = len(A)    
b = len(B)    
s=''
while a>0 and b>0:
    # dp[a-1][b] == dp[a][b-1]?
    if dp[a][b] !=dp[a-1][b] and dp[a][b] !=dp[a][b-1]:
        if dp[a-1][b]==0 and dp[a][b-1]==0:
            s=A[a-1]+s
            break
        s=A[a-1]+s
        a-=1
        b-=1
    elif dp[a][b] ==dp[a-1][b]:
        a-=1
    elif dp[a][b] ==dp[a][b-1]:
        b-=1

print(dp[len(A)][len(B)])
if s:
    print(s)
'''
ACAYKP
CAPCAK
'''