import sys
input=sys.stdin.readline
n = int(input())
board = [[" " for i in range(n)] for j in range(n)] 

for i in range(n):
    board[i] = list(map(str, input().rstrip("\n")))

cnt = 1
ans = 1

def check(i, j):
    cnt = 1
    global ans
    # 가로 탐색
    for k in range(n-1):
        if board[i][k] == board[i][k+1]:
            cnt += 1
            ans = max(ans, cnt)
            
        else:
            ans = max(ans, cnt)
            cnt = 1
    cnt = 1
    if i < n-1:
        for k in range(n-1):
            if board[i+1][k] == board[i+1][k+1]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                ans = max(ans, cnt)
                cnt = 1
    cnt = 1
    # 세로 탐색
    for k in range(n-1):
        if board[k][j] == board[k+1][j]:
            #print(k, j, k+1, j, 'conn')
            cnt += 1
            ans = max(ans, cnt)
        else:
            #print(k, j, k+1, j, 'x')
            ans = max(ans, cnt)
            cnt = 1
    cnt = 1
    if j < n-1:
        for k in range(n-1):
            if board[k][j+1] == board[k+1][j+1]:
                #print(k, j+1, k+1, j+1, 'conn')
                cnt += 1
                ans = max(ans, cnt)
            else:
                ans = max(ans, cnt)
                #print(k, j+1, k+1, j+1, 'x')
                cnt = 1

for i in range(n):
    for j in range(n-1):
        # 행에서 바꾸기
        temp = board[i][j]
        board[i][j] = board[i][j+1]
        board[i][j+1] = temp
        #print(i, j, i, j+1)
        check(i, j)
        temp = board[i][j+1] # 원래 j자리에 들어가야 할 수
        board[i][j+1] = board[i][j]
        board[i][j] = temp

        # 열에서 바꾸기
        temp = board[j][i]
        board[j][i] = board[j+1][i]
        board[j+1][i] = temp
        #print(j, i, j+1, i)
        check(j, i)
        temp = board[j+1][i]
        board[j+1][i] = board[j][i]
        board[j][i] = temp
print(ans)