'''
dice
  2
4 1 3
  5
  6

  - 위아래 합 7

dice = list(range(1, 1 + 6))


top
north
east
south
west
bottom


E
top, north, east, south, west, bottom = east, north, bottom, south, top, bottom

W
top, north, east, south, west, bottom = west, north, top, south, bottom, east

N
top, north, east, south, west, bottom = north, bottom, east, top, west, south

S
top, north, east, south, west, bottom = south, top, east, bottom, west, north

'''
dice = [0] * 6
top, north, east, south, west, bottom = 0, 1, 2, 3, 4, 5

n, m, y, x, k = map(int, input().split())
ans = 0
board = [[ *map(int, input().split())] for _ in range(n)]

dice[bottom] = board[y][x]
L = [*map(int, input().split())]

def bound(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    else:
        return False

def E():
    global ans, y, x, top, north, east, south, west, bottom
    ny, nx = y, x + 1
    if not bound(ny, nx):
        return
    top, north, east, south, west, bottom = east, north, bottom, south, top, west
    if not board[ny][nx]:
        board[ny][nx] = dice[bottom]
    else:
        dice[bottom] = board[ny][nx]
        board[ny][nx] = 0
    y, x = ny, nx
    print(dice[top])


def W():
    global ans, y, x, top, north, east, south, west, bottom
    ny, nx = y, x - 1
    if not bound(ny, nx):
        return
    top, north, east, south, west, bottom = west, north, top, south, bottom, east
    if not board[ny][nx]:
        board[ny][nx] = dice[bottom]
    else:
        dice[bottom] = board[ny][nx]
        board[ny][nx] = 0
    y, x = ny, nx
    print(dice[top])

def N():
    global ans, y, x, top, north, east, south, west, bottom
    ny, nx = y - 1, x
    if not bound(ny, nx):
        return
    top, north, east, south, west, bottom = north, bottom, east, top, west, south
    if not board[ny][nx]:
        board[ny][nx] = dice[bottom]
    else:
        dice[bottom] = board[ny][nx]
        board[ny][nx] = 0
    y, x = ny, nx
    print(dice[top])

def S():
    global ans, y, x, top, north, east, south, west, bottom
    ny, nx = y + 1, x
    if not bound(ny, nx):
        return
    top, north, east, south, west, bottom = south, top, east, bottom, west, north
    if not board[ny][nx]:
        board[ny][nx] = dice[bottom]
    else:
        dice[bottom] = board[ny][nx]
        board[ny][nx] = 0
    y, x = ny, nx
    print(dice[top])


for order in L:
    if order == 1:
        E()
    elif order == 2:
        W()
    elif order == 3:
        N()
    else:
        S()