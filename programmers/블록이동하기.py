n,m=0,0
dp=[]
Dy= [0,0,1,-1]
Dx= [1,-1,0,0]
b=[]
def rec(Y,X,y,x):
    if (y,x)==(n-1,m-1):
        return
    if Y==y: # 가로
        right_1by2(y,x)
        left_1by2(Y,X)
        
    global n,m
    
    
def cw0(y,x):
    if not b[y-1][x] and not b[y-1][x]:


def cw90():

def cw180():

def cw270():

def ccw0():

def ccw90():

def ccw180():

def ccw270():

def mvr_1by2():

def mvr_2by1():

def mvl_1by2():

def mvr_2by1():


def right_1by2(y,x):
    if not b[y][x+1]:
        if dp[y][x]+1<dp[y][x+1]:
            dp[y][x+1]=dp[y][x]+1
            rec(y,x,y,x+1)
  
def left_1by2(Y,X):
    if not b[Y][X-1]:
        if dp[Y][X]+1<dp[Y][X-1]:
            dp[Y][X-1]=dp[Y][X]+1
            rec(Y,X-1,Y,X)
            dp[ny][nx][0]= min(dp[y][x][0]+1)
def solution(board):
    n= len(board)
    m= len(board[0])
    b=[[1]*(m+2)]
    b+=[[1]+el[:]+[1] for el in board]
    b+=[[1]*(m+2)]
    
    
    dp= [[[1e9]*2 for __ in range(len(m+2))] for _ in range(n+2)]
    dp[0][0]=0
    dp[0][1]=0
    rec(0,0,0,1)
    return dp[n-1][m-1]

# 10000000