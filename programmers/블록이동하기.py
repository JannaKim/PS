from heapq import heappush, heappop

r , c = -1e9 , -1e9
h , v = 0 , 1
B = []
dp_verti = []
dp_hori = []
q = []
def bound_chk(y , x):
    global r , c
    if 0 <= y < r and 0 <= x < c:
        return True
    return False

'''
    head:
    xo

    x
    o
''' 
def rotate_down(step , y , x):
    global v , h , q , dp_hori , dp_verti
    if bound_chk(y + 1 , x - 1) and not B[y + 1][x - 1]:
        if bound_chk(y + 1 , x) and not B[y + 1][x]:

            if step + 1 < dp_verti[y + 1][x - 1]:
                dp_verti[y + 1][x - 1] = step + 1
                heappush(q , (step + 1 , v ,  y + 1 , x - 1))

            if step + 1 < dp_verti[y + 1][x]:
                dp_verti[y + 1][x] = step + 1
                heappush(q , (step + 1 , v , y + 1 , x))


def rotate_up(step , y , x):
    global v , h , q , dp_hori , dp_verti 
    if bound_chk(y - 1 , x - 1) and not B[y - 1][x - 1]:
        if bound_chk(y - 1 , x) and not B[y - 1][x]:

            if step + 1 < dp_verti[y][x - 1]:
                dp_verti[y][x - 1] = step + 1
                heappush(q , (step + 1 , v , y , x - 1))

            if step + 1 < dp_verti[y][x]:
                dp_verti[y][x] = step + 1
                heappush(q , (step + 1 , v , y , x))

def hori_moves_right(step , y , x):
    global v , h , q , dp_hori , dp_verti 
    if bound_chk(y , x + 1) and not B[y][x + 1]:
        if step + 1 < dp_hori[y][x + 1]:
            dp_hori[y][x + 1] = step + 1
            heappush(q , (step + 1 , h , y , x + 1))

def hori_moves_left(step , y , x):
    global v , h , q , dp_hori , dp_verti 
    if bound_chk(y , x - 2) and not B[y][x - 2]:
        if step + 1 < dp_hori[y][x - 2]:
            dp_hori[y][x - 1] = step + 1 # 머리는 이쪽
            heappush(q , (step + 1 , h , y , x - 1))


def next_for_hori(step , y , x): # ㅡ
    rotate_down(step , y , x)
    rotate_up(step , y , x)
    hori_moves_right(step , y , x)
    hori_moves_left(step , y , x)




def rotate_right(step , y , x):
    global v , h , q , dp_hori , dp_verti
    if bound_chk(y - 1 , x + 1) and B[y - 1][x + 1]:
        if bound_chk(y , x + 1) and B[y][x + 1]:
            if step + 1 < dp_hori[y - 1][x + 1]:
                dp_hori[y - 1][x + 1] = step + 1
                heappush(q , (step + 1 , h,  y - 1 , x + 1))

            if step + 1 < dp_hori[y][x + 1]:
                dp_hori[y][x + 1] = step + 1
                heappush(q , (step + 1 , h , y , x + 1))

def rotate_left(step , y , x):
    global v , h , q , dp_hori , dp_verti
    if bound_chk(y - 1 , x - 1) and B[y - 1][x - 1]:
        if bound_chk(y , x - 1) and B[y][x - 1]:
            if step + 1 < dp_hori[y - 1][x]:
                dp_hori[y - 1][x] = step + 1
                heappush(q , (step + 1 , h,  y - 1 , x))

            if step + 1 < dp_hori[y][x]:
                dp_hori[y][x] = step + 1
                heappush(q , (step + 1 , h , y , x))


def verti_moves_right(step , y , x):
    global v , h , q , dp_hori , dp_verti
    if bound_chk(y , x + 1) and not B[y][x + 1]:
        if bound_chk(y - 1 , x + 1) and not B[y - 1][x + 1]:
            if step + 1 < dp_verti[y][x + 1]:
                dp_hori[y][x + 1] = step + 1 # 머리는 이쪽
                heappush(q , (step + 1 , v , y , x + 1))

def verti_moves_left(step , y , x):
    global v , h , q , dp_hori , dp_verti
    if bound_chk(y , x - 1) and not B[y][x - 1]:
        if bound_chk(y - 1 , x - 1) and not B[y - 1][x - 1]:
            if step + 1 < dp_verti[y][x - 1]:
                dp_hori[y][x - 1] = step + 1 # 머리는 이쪽
                heappush(q , (step + 1 , v , y , x - 1))

def next_for_verti(step , y , x):
    rotate_right(step , y , x)
    rotate_left(step , y , x)
    verti_moves_right(step , y , x)
    verti_moves_left(step , y , x)

    


def bfs():
    global r , c , q

    heappush(q , (0 , 0 , 0 , 1))
    '''
    head:
    xo

    x
    o
    ''' 
    while q:
        step , direct , y , x = heappop(q)
        print(step , direct , y , x)
        if y == r - 1 and x == c - 1:
            return step

        if not direct: # hori
            next_for_hori(step , y , x)
        
        else:
            next_for_verti(step , y , x)

def solution(b):
    global r , c , B , dp_verti , dp_hori
    r = len(b)
    c = len(b[0])
    dp_verti = [[int(1e9)] * c for _ in range(r)]
    dp_hori = [[int(1e9)] * c for _ in range(r)]
    dp_hori[0][1] = 0
    B = [el[:] for el in b]
    answer = bfs()

    return answer

# 10000000
print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))