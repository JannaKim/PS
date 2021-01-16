import sys; sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().rstrip()
n=int(input())
paper=[[-1]*(n+1)]
paper+=[[-1]+ [*map(int, input().split())] for _ in range(n)]

#[print(*el) for el in paper]



def isWhite(sy, sx, ey, ex):
    for i in range(sy, ey+1):
        for j in range(sx,ex+1):
            if paper[i][j]==1:
                return False
    return True

def isBlue(sy, sx, ey, ex):
    for i in range(sy, ey+1):
        for j in range(sx,ex+1):
            if paper[i][j]==0:
                return False
    return True

white=0
blue=0
def cut(sy, sx, ey, ex):
    global white
    global blue
    if isWhite(sy, sx, ey, ex): 
        white+=1 
        return
    if isBlue(sy, sx, ey, ex): 
        blue+=1
        return
    cut(sy, sx, (sy+ey)//2, (sx+ex)//2)# 왼위
    cut((sy+ey)//2+1, sx, ey, (sx+ex)//2) # 왼아
    cut(sy, (sx+ex)//2+1, (sy+ey)//2, ex) # 오위
    cut((sy+ey)//2+1, (sx+ex)//2+1, ey, ex) #오아

cut(1,1,n,n)    
print(white)
print(blue)