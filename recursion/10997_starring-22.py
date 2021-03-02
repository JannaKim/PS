import time
n= int(input())
'''
가로
1
1+4
1+4+4

세로: 가로+2
'''

width= 1+(n-1)*4
height= width+2
mp= [ [' ']*(width) for _ in range(height)]

#[print(*el) for el in mp]

y= 0
x= width-1


def draw(y,x,roof):
    w= roof
    h= roof+2
    for i in range(roof):
        mp[y][x+i]= '*'
        mp[y+h-1][x+i]='*'
    for i in range(h):
        mp[y+i][x]='*'
    for i in range(h-2):
        mp[y+2+i][x+w-1]='*'

    for i in range(2):
        mp[y+2][x+roof-1-i]='*'
    
    if roof==5:
        mp[y+2][x+2]='*'
        mp[y+2+1][x+2]='*'
        mp[y+2+1+1][x+2]='*'
        return
    #[print(*el) for el in mp]
    draw(y+2, x+2, roof-4)

if n==1:
    print('*')
else:
    draw(0,0,width)
    for line in mp:
        while line[-1]==' ':
            line.pop()
        print(''.join(line))
