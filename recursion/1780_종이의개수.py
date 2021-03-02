import sys; input = lambda: sys.stdin.readline().rstrip(); r = range

n= int(input())
paper=[]
for i in range(n):
    paper.append([*map(int, input().split())])
k=-1
for i in range(8):
    if 3**i==n:
        k=i
        break

stock=[0]*3
def rec(y, x, k):
    if k==0:
        stock[paper[y][x]+1]+=1
        return
    s= 0
    flag=True
    val= paper[y][x]
    for i in r(y, y+3**k):
        for j in r(x, x+3**k):
            if paper[i][j]!=val:
                flag=False
                break
            s+= paper[i][j]
    if flag:
        if s==0:
            stock[1]+=1
            return
        elif s==(3**k)**2:
            stock[2]+=1
            return
        elif s==-((3**k)**2):
            stock[0]+=1
            return
    else:
        onethird= 3**(k-1)
        rec(y, x, k-1)
        rec(y, x+onethird, k-1)
        rec(y, x+2*onethird, k-1)
        rec(y+onethird, x, k-1)
        rec(y+onethird, x+onethird, k-1)
        rec(y+onethird, x+2*onethird, k-1)
        rec(y+2*onethird, x, k-1)
        rec(y+2*onethird, x+onethird, k-1)
        rec(y+2*onethird, x+2*onethird, k-1)

rec(0, 0, k)
[print(el) for el in stock]


