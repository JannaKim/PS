c, r= map(int, input().split())
k=int(input())

def rec(y, x, w, h, k):
    grid=w*h-(w-2)*(h-2)
    if k<=grid:
        if k<=h:
            return (y, x+k-1)
        elif k<=w+h-1:
            k-=h
            return (y+k,x+(h-1)) 
        elif k<=2*h+w-2:
            k=k-h-w+1
            return (y+(w-1),x+h-1-k) 
        else:
            k=k-2*h-(w-2)
            return (y+w-1-k, x)

    else:
        if w-2<=0 or h-2<=0:
            return 0
        return rec(y+1, x+1,w-2,h-2,k-grid)

ans=rec(1,1,c,r,k)
if ans==0:
    print(ans)
else:
    print(*ans)


'''
di=[0,1,0,-1]
dj=[1,0,-1,0]

R,C=map(int,input().split())
N=int(input())
arr = [[0]*C for _ in range(R)]

i=0
j=0
d=0

num=1

if N > R*C:
    print(0)
    
while num <=R*C:

    arr[i][j]=num

    num+=1

    ni = i+di[d]
    nj = j+dj[d]

    if 0<=ni<R and 0<=nj<C and arr[ni][nj]==0:
        i,j = ni,nj
    else:
        d = (d+1)%4
        i += di[d]
        j += dj[d]

flag=0
# #2.답 출력
for i in range(R):
    for j in range(C):
        if arr[i][j] == N:
            print(i+1,j+1)
            flag=1
            break
    if flag:
        break


'''