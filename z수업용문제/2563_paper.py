paper=[]
for _ in range(100):
    paper.append([0]*100) # 도화지 만들고

n= int(input())
for _ in range(n):
    y, x=map(int, input().split()) 
    x-=10 # 받은 색종이의 왼쪽 위 좌표 구해야하는데 x좌표는 10만큼 위로 올리면 됨
    for i in range(y,y+10):
        for j in range(x,x+10):
            paper[i][j]=1 # 종이 붙어있는곳도 그냥 계속 1로 덮어씌우면 된다.

ans=0
for i in range(100):
    for j in range(100):
        if paper[i][j]:
            ans+=1 # 칠해진애 다 더하면 총 넓이이다.
print(ans)