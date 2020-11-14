'''
line, row = list(map(int,input().split()))

mp=[]
mp.append(' '*(row+2))
for _ in range(line):
    mp.append(' '+input()+' ')
mp.append(' '*(row+2))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
mx=0

q = [((1, 1), 1)]
chk = [False]*(91-65)

while q:
    node, ans = q.pop()
    i, j = node
    for x,y in zip(dx,dy):
        if mp[i+x][j+y] != ' ' and chk[ord(mp[i+x][j+y])-65]==False:
            chk[ord(mp[i+x][j+y])-65] = True
            q.append(((i+x, j+y), ans + 1))
            print(q)
            chk[ord(mp[i+x][j+y])-65] = False

print(ans)
'''

line, row = list(map(int,input().split()))

mp=[]
mp.append(' '*(row+2))
for _ in range(line):
    mp.append(' '+input()+' ')
mp.append(' '*(row+2))

dx = [1, 0,-1,  0]
dy = [0, -1,0,  1]
mx=0



dic = {}
for i in range(65,91):
    dic[chr(i)] = False

dic[mp[1][1]] = True

q = [(1, 1, dic)]
while q:
    i, j, dic = q.pop(0)
    mx = max(mx, sum(1 for s in dic.values() if s==True))
    if mx == 26: break
    for y,x in zip(dx,dy):
        if mp[i+x][j+y] != ' ' and dic[mp[i+x][j+y]]== False:
            dic[mp[i+x][j+y]]= True
            q.append((i+x, j+y, dic))
            dic[mp[i+x][j+y]]= False

print(mx)

'''
2 4
CAAB
ADCB

5 4
ABCD
CAEA
DAFA
EGFK
ZAAA

'''