#dp[i][j]: i*j로 점프할 수 있는 경우의 수
N = int(input())
board=[]
dp=[]
for _ in range(N):
    dp.append([0]*N)
    board.append([int(i) for i in input().split()])
#[print(a) for a in board]

dp[0][0]=1
for i in range(N):
    for j in range(N): #  y좌표 ix좌표 j, [i,j]
        if i==0: # 1행이라면
            for k in range(j):
                if j-k==board[i][k]:
                    dp[i][j]+=dp[i][k]
                    #print(f"board[{i}][{k}] 에서 board[{i}][{j}]로 점프 가능1")
        elif j==0: # 1열이라면
            for k in range(i):
                if i-k==board[k][j]:
                    dp[i][j]+=dp[k][j]
                    #print(f"board[{k}][{j}] 에서 board[{i}][{j}]로 점프 가능2")
        else:
            for a in range(i):
                if i-a==board[a][j]:
                    dp[i][j]+=dp[a][j]  
                    #print(f"board[{a}][{j}] 에서 board[{i}][{j}]로 점프 가능3")
            for b in range(j):
                if j-b==board[i][b]:
                    dp[i][j]+=dp[i][b] 
                    #print(f"board[{i}][{b}] 에서 board[{i}][{j}]로 점프 가능4")

#[print('\t\t',a) for a in dp]
print(dp[N-1][N-1])

'''
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0
'''

