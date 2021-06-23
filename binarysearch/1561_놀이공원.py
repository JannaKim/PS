n, m = map(int, input().split())
L=[*map(int, input().split())]
lo = -1
hi = 2 * int(1e9) * 30

def cal(k):
    global m 
    s = 0
    for el in L:
        s += (k // el + 1)
    return s

time = 0
while lo <= hi:
    mid = (lo + hi) // 2
    if cal(mid) < n:
        time = mid
        lo = mid + 1
        
    else:
        hi = mid -1
        


#print(cal(time), cal(time+1) )
if time<0:
    print(n)
else:
    #print(time, cal(time))
    remain = n - cal(time)
    q = []
    A = []
    for i in range(m):
        if not (time+1) % L[i]:
            remain -=1
        if not remain:
            print( i+ 1)
            break


'''
10초 갈렸더니 모든 사람이 다 탑승했다
그 바로 직전은 9
진짜 진짜 진짜 진짜 진짜 진짜 진짜 진짜 진짜 진짜 진짜 어렵다
아이디어의 특징
dp : 조합을 전구간에 탐색하기가 힘들어서 스테이지별로 만들어야한다.

놀이 기구 이분 탐색할  때
특 정시간 내에 다 탐색할때
타임이라는 배열에다가 
시간 5로 운행되는 기계
탐승 한거니까 올리면 됨


dp
bfs
dfs
bs
dijikstra
시작 초기화 
bellman
union find
'''