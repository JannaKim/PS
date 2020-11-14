from sys import *
input= lambda: stdin.readline().rstrip()
line, row = list(map(int,input().split()))

mp=[]
mp.append(' '*(row+2))
for _ in range(line):
    mp.append(' '+input()+' ')
mp.append(' '*(row+2))


'''
2 4
CAAB
ADCB

3 3
AAC
CAA
ESQ

4 3
JID
ABC
BGF
IHJ
'''

dx = [0,0,1,-1]
dy = [1,-1,0,0]
mx=1
def f(i,j,data):
    #print(data)
    global mx
    mx = max(mx,len(data))
    if mx==26:
        print(26)
        exit()
    for x,y in zip(dx,dy):
        if mp[i+x][j+y] != ' ' and mp[i+x][j+y] not in data:    
            f(i+x,j+y,data+mp[i+x][j+y])
f(1,1,mp[1][1])
print(mx)