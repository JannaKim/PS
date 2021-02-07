import sys; input= lambda: sys.stdin.readline().rstrip()
n= int(input())
m= int(input())
dp= [["100"]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c= input().split()
    if eval(dp[int(a)][int(b)])>eval(c):
        dp[int(a)][int(b)]= c

for i in range(1, n+1): # 중간에 이 간선 끼워넣음
    for j in range(1, n+1):
        print([dp[i][j], 0][dp[i][j]=="10000000"], end=' ')
    print()

for i in range(1, n+1): # 중간에 이 간선 끼워넣음
    dp[i][i]='0'
    for j in range(1, n+1):
        for k in range(1, n+1):
            print(f'dp[{j}][{k}]= min(dp[{j}][{k}], dp[{j}][{i}]+dp[{i}][{k}])')
            if eval(dp[j][i]+'+'+dp[i][k])<eval(dp[j][k]):
                print(f'dp[{j}][{k}]= {dp[j][k]}-> dp[{j}][{i}]+dp[{i}][{k}]= {dp[j][i]+"+"+dp[i][k]}')
                dp[j][k]=dp[j][i]+'+'+dp[i][k]
for i in range(1, n+1): # 중간에 이 간선 끼워넣음
    for j in range(1, n+1):
        print([dp[i][j], 0][dp[i][j]=="10000000"], end=' ')
    print()