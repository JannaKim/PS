# X 보면 stc 에 넣음 , chk , 재귀는 안함
# 같은 . 이면 chk 후 재귀

Dy = [0 , 0 , 1 , -1]
Dx = [1 , -1 , 0 , 0]

r , c = map(int, input().split())

# 확인. 초기화안함
chk =  [[ 0 ] * c for _ in range(r)]
mp = [ list(input()) for _ in range(r)]
'''
1 녹
2 백조
'''
'''
melted 처음에 . ,   L 넣고 시작 , chk도 함

리스트 모으는거 길텐데?

백조 먼저 L ,R

처음부터 만났을땐?
'''
swan = []
# swan first
for i in range(r):
    for j in range(c):
        if mp[i][j] == 'L':
            swan.append( (i , j) )
melted = []
siren = False

def bound(y , x):
    if 0 <= y < r and 0 <= x <c:
        return True
    return False

def met(a , b , c , d):
    if chk[a][b] * chk[c][d] > 40:
        return True
    return False

def swim(y , x):
    stc = [(y , x)]
    for dy , dx in zip(Dy , Dx):
        ny = y + dy 
        nx = x + dx
        if bound(ny , nx) and chk[ny][nx] != chk[y][x]:
            if mp[ny][nx] == 'X':
                continue

            else:
                if mp[ny][nx] == '.':
                    chk[ny][nx] = chk[y][x] # swan으로 색칠
                    stc += swim(ny , nx)
                elif met(y , x , ny , nx):
                    global siren
                    siren = True
                    return
    return stc

for idx , (y , x) in enumerate(swan):
    chk[y][x] = idx + 6
    melted += swim(y , x )

[print(*el) for el in chk]
if siren:
    print(0)
    exit()

# . 차례

for i in range(r):
    for j in range(c):
        if mp[i][j] == '.':
            melted.append( (i , j) )
#print(melted)
'''
def broadenSwan(y , x , intact, changed):
    for dy , dx in zip(Dy , Dx):
        ny = y + dy
        nx = x + dx
        if bound(ny , nx) and chk[ny][nx] == intact:
            chk[ny][nx] = changed
            broadenSwan(y , x , intact, changed):


if chk[y][x] != chk[ny][nx]:
    X 면 같은 chk로 바꿈
    둘이 곱해서 4되면.
    아니면 합쳐진다.
    if a<b:
        broadenSwan(a , a to b)
    big = max()
    small = max()
    flood()
'''