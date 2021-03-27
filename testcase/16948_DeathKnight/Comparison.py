from collections import deque
n=200
for i in range(200):
    for j in range(200):
        for k in range(200):
            for l in range(200):
                a, b, x, y= k, l, i, j
                Y, X, A, B= k, l, i, j
                if (k,l)==(i,j):
                    continue
                if a==x and b!=y:
                    continue
                if a!=x and b==y:
                    continue

                math_ans=-1

                def math():
                    global a, b, x, y, n, math_ans
                    if a>=n or b>=n or x>=n or y>=n or a<0 or b<0 or x<0 or y<0:
                        print(-1)
                        exit()

                    if a==x and b!=y:
                        if abs(b-y)%2:
                            return
                              
                        else:    
                            math_ans=abs((b-y)//2)
                            
                    elif a!=x and b==y:
                        if not abs(a-x)%4:
                            math_ans=abs((a-x)//2)
                        return

                    elif a==x and b==y:
                        return
                    else:
                        if b>y:
                            a, x= x,a
                            b, y= y,b
                        cnt=0
                        if abs(a-x)%2:
                            return
                    # cnt+=abs(a-b)//2
                        while a!=x and b!=y:
                            b+=1
                            if a>x:
                                a-=2
                            else:
                                a+=2
                            cnt+=1

                        #math_ans= cnt
                        if b!=y and a==x:
                            if abs(b-y)%2:
                                return  
                            cnt+=abs(b-y)//2
                            math_ans= cnt
                        
                        elif a!=x and b==y:
                            if abs(a-x)%4:
                                return 
                            cnt+=abs(a-x)//2
                            math_ans= cnt
                        else:
                            math_ans=cnt

                math()



                bfs_ans=-1
                board= [[False]*n for _ in range(n)]

                board[Y][X]=True

                #y, x, a, b= map(int, input().split())

                dir= [(-2,-1), (-2,1), (0,-2), (0,2), (2,-1), (2,1)]

                q=[]
                q=deque()
                q.append((Y,X,0))
                flag=True

                while q:
                    r, c, mv= q.popleft()
                    if (r,c)== (A,B):
                        bfs_ans= mv
                        flag=False
                        break

                    for dy, dx in dir:
                        if r+dy>=n or c+dx>=n or r+dy<0 or c+dx<0:
                            continue
                        if not board[r+dy][c+dx]:
                            board[r+dy][c+dx]=True
                            q.append((r+dy, c+dx,mv+1))


                if math_ans!=bfs_ans:
                    print(f'{Y} {X}-> {A} {B} {math_ans}!={bfs_ans}' )
                    exit()


print('same code!')