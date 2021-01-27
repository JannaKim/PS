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


def erase(a, b, size):
    for i in r(a, a+size):
        for j in r(b, b+size):
            paper[i][j]=0


def repaste(a, b, size):
    
    for i in r(a, a+size):
        for j in r(b, b+size):
            paper[i][j]=1
    #print('repasted', size)
    #[print(*el) for el in paper]
    #print()


stock= [1e9, 5, 5, 5, 5, 5]


mn= 1e9

def backtrack(a,b,cnt):  

    global mn

    for i in r(1,6):
        if stock[i]<0: return

    isValid=True
    for i in r(1,11):
        for j in r(1,11):
            if paper[i][j]!=0:
                isValid=False
                break
    if isValid:
        #print('Valid',cnt)
        mn= min(mn, cnt)
        #if mn==4: sys.exit()
        return

    
    #print(a, b, cnt)
    #print(stock)
    #[print(*el) for el in paper]
    #print()
    for i in r(1,11):
        for j in r(1,11):
            if paper[i][j]:
                paper[i][j]=0
                biggest=5
                for k in r(1,5):
                    if not widen(i,j+k,(k+1)*2-1,k+1): 
                        biggest=k   
                        break
                    # 한칸더 큰 색종이 붙일 수 있으면

                for d in r(biggest, 0, -1):
                    erase(i, j, d)
                    
                    stock[d]-=1
                    backtrack(i, j, cnt+1)
                    stock[d]+=1
                    repaste(i, j, d)
                return


    

backtrack(1, 1,  0)

print([mn, -1][mn==1e9])



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


'''
def Check(i, j, m):
    for x in range(i, i + m):
        for y in range(j, j + m):
            if matrix[x][y] == 0:
                return False
    return True

def MakeReverse(i, j, m, a):
    for x in range(i, i + m):
        for y in range(j, j + m):
            matrix[x][y] = a
            
def solve(a):
    if sum(frequency) >= result[0]:
        return
    for i in range(a,10):
        for j in range(10):
            if matrix[i][j] == 1:
                for k in range(5,0,-1):
                    if i < 11-k and j < 11-k and frequency[k] < 5:
                        if Check(i, j, k):
                            MakeReverse(i, j, k, 0)
                            frequency[k] += 1
                            solve(i)
                            frequency[k] -= 1
                            MakeReverse(i, j, k, 1)
                return
    result[0] = min(result[0],sum(frequency))

matrix = [list(map(int,input().split())) for _ in range(10)]
frequency = [0 for _ in range(6)]
result = [987654321]
solve(0)
if result[0] == 987654321:
    print(-1)
else:
    print(result[0])
'''