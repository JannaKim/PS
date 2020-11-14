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
    global mx
    for x,y in zip(dx,dy):
        chk=0
        if 0 < i+x and i+x<line+2 and 0< j+y and j+y<row+2 and mp[i+x][j+y] != ' ' and data[ord(mp[i+x][j+y])-65]==' ':
            if ord(mp[i+x][j+y])-65==0:
                data ='V'+data[1:]
                mx = max(mx,data.count('V'))
                f(i+x,j+y,data)
                data = ' '+data[1:]
            elif ord(mp[i+x][j+y])-65==26:
                data = data[:-1]+'V'
                mx = max(mx,data.count('V'))
                f(i+x,j+y,data)
                data = data[:-1]+' ' 
            else:
                data = data[:ord(mp[i+x][j+y])-65]+'V'+data[ord(mp[i+x][j+y])-65+1:]
                mx = max(mx,data.count('V'))
                f(i+x,j+y,data)
                data = data[:ord(mp[i+x][j+y])-65]+' '+data[ord(mp[i+x][j+y])-65+1:]
                


s=' '*(91-65)
s = s[:ord(mp[1][1])-65]+'V'+s[ord(mp[1][1])-65+1:]

f(1,1,s)
print(mx)


