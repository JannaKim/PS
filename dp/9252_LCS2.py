A = input()
B = input()

dp=[]
for i in range(len(B)+2):
    dp.append([0]*(len(A)+2))

for i in range(1,len(B)+1):
    for j in range(1,len(A)+1):
        if A[j-1]==B[i-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])

'''
ACCA
ABCACA
'''
b = len(B)
a = len(A)

s=''
while a>0 and b>0:
    if dp[b][a]!=dp[b-1][a] and dp[b][a]!=dp[b][a-1]:
        s= A[a-1] + s
        a-=1
        b-=1
    elif dp[b][a] == dp[b-1][a]:
        b-=1
    else:
        a-=1
print(s)
