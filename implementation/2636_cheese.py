'''
거쳐갔으면 chk
dy dx 돌렸는데 체크 안돼있고 치즈면 체크, 넣고 끝
dy dx 돌렸는데 체크 안돼있고 치즈아니면 체크, 뉴큐엔 안넣고 bfs큐에 다시 넣음
'''
from collections import deque
r , c = map(int , input().split())
mp = [ [*map(int , input().split())] for _ in range(r)]
chk = [ [0] * c for _ in range(r) ] 
cheese = deque()
cheese.append ((0 , 0))
chk[0][0] = 1
Dy = [0 , 0 , 1 , -1]
Dx = [1 , -1 , 0 , 0]

last_slices=0
t = 0
while True:
    new_cheese = deque()
    while cheese:
        y , x = cheese.popleft()
        for dy , dx in zip(Dy , Dx):
            ny = y + dy
            nx = x + dx
            if 0 <= ny < r and 0 <= nx < c:
                if not chk[ny][nx] and mp[ny][nx]:
                    new_cheese.append( (ny , nx) )
                    chk[ny][nx] = 1
                elif not chk[ny][nx] and not mp[ny][nx]:
                    cheese.append( (ny , nx) )
                    chk[ny][nx] = 1

    if not new_cheese:
        break
    cheese.clear()
    for el in new_cheese:
        cheese.append( (el) )
    last_slices = len(new_cheese)
    t += 1

print(t , last_slices , sep = '\n')

    


'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''