# dp[i][j]: 숫자i를 숫자 1~j 조합으로 만드는 모든 경우
#dp=[[[]],[[],[]],[[],[],[]],[[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[],[]]]

N=int(input())
P=[int(i) for i in input().split()]
dp=[]
for a in range(N+1):
    dp.append([])
    for b in range(a+1):
        dp[a].append([])

for i in range(1,N+1):
    for j in range(1,i+1):
        for k in range(j,0,-1): # k는 큰돌
            #print(f"j-k={j-k}, j={j}")
            if i-k>k:
                print(f"{'       '}dp[{i}][{j}] += 큰돌[{k}]와 dp[{i-k}][{k}] 조합")
                if not dp[i-k][k]:
                    dp[i][j].append([k])
                for l in dp[i-k][k]:
                    dp[i][j].append([k]+l)
            else:
                print(f"{'       '}dp[{i}][{j}] += 큰돌[{k}]와 dp[{i-k}][{i-k}] 조합")
                if not dp[i-k][i-k]:
                    dp[i][j].append([k])
                for l in dp[i-k][i-k]:
                    dp[i][j].append([k]+l)
        print(f"dp[{i}][{j}]={dp[i][j]}")
mx=0      
for seq in dp[N][N]:
    occ=0
    for nm in seq:
        occ+=P[nm-1]
    if mx<occ:
        mx=occ
print(mx)
