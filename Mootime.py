import sys
import time


mooLen = [0 for i in range(100)]
N = int(sys.stdin.readline())

# S(0), S(1), S(2) ... 각 항의 길이를 list에 저장
mooLen[0] = 3
for i in range(1, 100):
    #mooLen[i] = (3+i)*(2**(i-1))-(3+i) 했더니 틀림.. 일반항 잘못 찾았나ㅜㅜ
    mooLen[i] = mooLen[i-1]*2 + i+3
    if(mooLen[i] > 1e9): break

print(mooLen[99])
def moo(n):
    # 앞쪽 moo에서 찾는 경우
    if(n <= 3):
        if(n == 1):
            return 'm'
        else: 
            return'o'
    # n이 몇 번째 항(수열)에 속하는지 찾기
    i = 1
    start = time.time()
    while(n > mooLen[i]):
        i += 1
    end = time.time()
    #print((end-start)*1000000)
    # mooo... 부분의 길이
    onlyMooLen = i+3 #=mooLen[i]-2*mooLen[i-1]

    if(n <= mooLen[i] - mooLen[i-1]): #moooo...에 속하는 경우
        if(n - mooLen[i-1] == 1):
            return 'm'
        else:
            return 'o'

    #moo.. 뒷쪽에 속하는 경우 i-1 수열에서 찾아야 함
    #N=20이면 20-15를 moo()의 파라미터로 해서 재귀호출. 위 과정 반복하도록 해야함
    #N=16이면 16-15=1을 파라미터로. 이 경우는 다 쪼개진 후 마지막 i-1 수열의 맨 앞 moo를 의미
    return moo(n-mooLen[i-1]-onlyMooLen)

ans = moo(N)
print(ans)