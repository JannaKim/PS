from collections import deque
n = -1
D = [(-1 , 0) , (0 , 1) , (1 , 0) , (0 , -1)]
B = -1
up = 0
right = 1
down = 2
left = 3
dic = {}
dic[0] = 'up'
dic[1] = 'right'
dic[2] = 'down'
dic[3] = 'left'

def possi(y , x):
    global n
    if y < 0 or y >= n or x < 0 or x >= n or B[y][x]:
        return False
    return True

def move(d , ay , ax , by , bx):
    ay += D[d][0]
    by += D[d][0]
    ax += D[d][1]
    bx += D[d][1]
    if possi(ay , ax) and possi(by , bx):
        return True
    return False

def rotate(y , x , tail , dest):
    # 목적지, 대각선 검사
    if possi(y + D[dest][0] , x + D[dest][1]) and possi(y + D[tail][0] + D[dest][0] , x + D[tail][1] + D[dest][1] ):
        return True
    return False

def bfs(dp):
    q = deque()
    # q.append((y , x , tail , step))
    q.append( (0 , 1 ,    3 , 0) )
    while q:
        y , x , tail , step = q.popleft()
        ty , tx = y + D[tail][0] , x + D[tail][1]
        
        for d in range(4):
            if move(d , y , x , ty , tx):
                ny = y + D[d][0]
                nx = x + D[d][1]
                if step + 1 < dp[ny][nx][tail]: # 위치 바뀜 , 꼬리 같음
                    dp[ny][nx][tail] = step + 1
                    q.append( (ny , nx , tail , step + 1) )

            if d % 2 == tail % 2: # 자신이거나 180는 안돌음
                continue

            #rotate(ori_tail , new_tail)
            if rotate(y , x , tail , d): # if possi(ry , rx) and possi( (ry + ty) // 2, (ry + tx) // 2): # 꼬리가 가는 방향 , 대각선 ??
                if step + 1 < dp[y][x][d]:
                    dp[y][x][d] = step + 1
                    q.append( (y , x , d , step + 1) ) # 위치 같음 , 꼬리 바뀜

            # 머리 꼬리 스왑
            y , x , ty , tx = ty , tx , y , x 
            if rotate(y , x , (tail + 2) % 4 , d): # 이 함수 바꿔주다 스왑 까먹음
                if step + 1 < dp[y][x][d]:
                    dp[y][x][d] = step + 1
                    q.append( (y , x , d , step + 1) ) # 위치 같음 , 꼬리 바뀜
            y , x , ty , tx = ty , tx , y , x




    global up , down , right , left
    cs = [1e9] * 4
    cs[0] = dp[n-1][n-1][up]
    cs[1] = dp[n-1][n-1][left]
    cs[2] = dp[n-2][n-1][down]
    cs[3] = dp[n-1][n-2][right]
    #print(cs)
    return min(cs)
            

        



def solution(b):
    global n , B
    B = [el[:] for el in b]
    n = len(b)
    dp = [ [ [1e9] * 4 for _ in range (n)] for _ in range(n)]
    # dir: 꼬리가 위, 오, 아, 왼
    dp[0][1][3] = 0
    answer = bfs(dp)
    return answer

#print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0]]))

#print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))

#print(solution( [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))

#print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))