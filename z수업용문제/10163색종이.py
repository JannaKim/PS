n= int(input())
board= [[-1]*(101)+[-2] for _ in range(101)]
board+= [[-2]*(101)]

for p in range(n):
    a, b, c, d= map(int, input().split())
    for i in range(a, a+c):
        for j in range(b, b+d):
            if board[i][j]!=-2:
                board[i][j]=p

for idx in range(n):
    s=0
    for i in range(101):
        for j in range(101):
            if board[i][j]==idx:
                s+=1
    print(s)