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

dx = [1, 0,-1,  0]
dy = [0, -1,0,  1]
mx=1
def f(i,j,data):
    [print(k,end='') for k,v in data.items() if v==True]
    print()
    global mx
    for y,x in zip(dx,dy):
        if 0 < i+x and i+x<line+2 and 0< j+y and j+y<row+2 and mp[i+x][j+y] != ' ' and data[mp[i+x][j+y]]==False:
            data[mp[i+x][j+y]]=True
            mx = max(mx,sum(1 for value in data.values() if value==True))
            f(i+x,j+y,data)
            data[mp[i+x][j+y]]=False

dic={}
for i in range(65,91):
    dic[chr(i)]=False
dic[mp[1][1]]=True

f(1,1,dic)
print(mx)