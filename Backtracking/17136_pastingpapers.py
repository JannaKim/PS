import sys; input= lambda: sys.stdin.readline().rstrip(); r=range
paper=[]
paper=[[-1]*12]
for _ in r(10):
    paper.append([-1]+[*map(int, input().split())]+[-1])
paper.append([-1]*12)


def widen(row, col, n,side):
    if not n: return True
    #[print(*el) for el in paper]
    a= paper[row][col]
    if a>0:
        paper[row][col]=0
        if n<=side:
            if not widen(row,col-1,n-1,side):
                paper[row][col]= a
                #[print(*el) for el in paper]
                return False
        else:
            if not widen(row+1,col,n-1,side):
                paper[row][col]= a
                #[print(*el) for el in paper]
                return False

    else:
        return False
    return True


cnt=0
stock= [0,5, 5, 5, 5, 5]
for i in r(1,11):
    for j in r(1,11):
        if paper[i][j]:
            cnt+=1
            paper[i][j]=0
            for k in r(1,11):
                if not widen(i,j+k,(k+1)*2-1,k+1): 
                    stock[k]-=1
                    print(stock)
                    if stock[k]<0:
                        print(-1)
                        sys.exit()
                    break
            #print(cnt)

#[print(*el) for el in paper]
print(cnt)

'''
0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 1 1 1 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0
0 0 0 1 1 1 1 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''