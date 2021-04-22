import time
for _ in range(int(input())):
    m, n, x, y= [int(i) for i in input().split()]
    x-=1
    y-=1

    if n<m:
        m, n= n, m
        x, y= y, x
    # m<n
    b= x
    cnt=x+1
    flag= False
    for _ in range(n):
        if b==y:
            flag=True
            print(cnt)
            break
        b = (b+m)%n  ##########
        cnt+=m
        
    if not flag:
        print(-1)
#11 13 6 5