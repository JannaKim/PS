'''
def solution(board):
    b= [[-1]*(len(board[0])+2)]
    b+=[[-1]+board[i]+[-1] for i in range(len(board))]
    b.append([-1]*(len(board[0])+2))
    #[print(*el) for el in b]
    answer = 0
    #print(b[1][2])
    dp=[]
    for i in range(len(b)):
        dp.append([False]*len(b[0])

    def go(x,y):
        s=0
        mx=1
        #print(x,y)
        for k in range(2,1001):
            if b[x+k-1][y+k-1]!=1:
                return mx
            for i in range(x,x+k):
                for j in range(y,y+k):
                    if b[i][j]!=1:                    
                        return mx
            mx=k

    ans=0
    for i in range(1,len(board)+1):
        for j in range(1,len(board[0])+1):
            if b[i][j]:
                ans= max(ans,go(i,j))
                if ans==1000:
                    return ans**2
    return ans**2
'''


def solution(board):
    b= [[0]*(len(board[0])+2)]
    b+=[[0]+board[i]+[0] for i in range(len(board))]
    b.append([0]*(len(board[0])+2))

    dp=[]
    for i in range(len(b)):
        dp.append([0]*len(b[0]))
    ans=0
    for i in range(1, len(board)+1):
        for j in range(1,len(board[0])+1):
            if b[i][j]:
                b[i][j] = min(b[i][j-1], b[i][j], b[i][j]) + 1

    for el in b:
        ans = max(max(el), ans)
        
    return ans**2

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])