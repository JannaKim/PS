line, row = list(map(int,input().split()))

mp=[]
mp.append(' '*(row+2))
for _ in range(line):
    mp.append(' '+input()+' ')
mp.append(' '*(row+2))

dx = [1, 0,-1,  0]
dy = [0, -1,0,  1]
mx=0

q = [(1, 1, mp[1][1])]
chk = []

while q:
    i, j, sentence = q.pop()
    mx = max(mx, len(sentence))
    if mx == 26: break
    for x,y in zip(dx,dy):
        if mp[i+x][j+y] != ' ' and mp[i+x][j+y] not in sentence:
            q.append((i+x, j+y, sentence + mp[i+x][j+y]))

print(mx)