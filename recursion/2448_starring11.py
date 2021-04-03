import sys; input= lambda: sys.stdin.readline().rstrip()
from math import log
n= int(input())
wid= 2*n-1
mp= [[' ']*(wid) for _ in range(n)]
#5 5*2+1 5*4+3 5*8+4
def star(y, x, h, w):
    if h==3: ###########
        a, b= y+2, x-2
        for _ in range(5):
            mp[a][b]='*'
            b+=1
        mp[y][x]='*'
        
        mp[y+1][x-1]='*'
        mp[y+1][x+1]='*'
        return
    #print(y, x, h, w)
    # draw triangle
    a, b= y, x
    for _ in range(h):
        mp[a][b]='*'
        a+=1
        b-=1
    
    #[print(*el) for el in mp]
    a, b= y, x
    for _ in range(h):
        mp[a][b]='*'
        a+=1
        b+=1
    #[print(*el) for el in mp]
    '''
    a, b= y+h-1, x-w//2
    for i in range(w):
        if i%6!=5:
            mp[a][b]='*'
        b+=1
    '''
    #[print(*el) for el in mp]

    star(y, x, h//2, w//2)
    star(y+h//2, x-h//2, h//2, w//2)
    star(y+h//2, x+h//2, h//2, w//2)


    # d and c

#print(wid)

star(0, wid//2, n, 5*n//3+int(log(n//3,2)))

for i in range(n):
    print(''.join(mp[i]))