def hanoi(n, start, end):
    if n==1:
        print(start, end)
        return
    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)




n= int(input())
#hanoi(n, 1, 3)

def tanoi(n, start, end, mid):
    if n==1:
        print(start, end)
        return
    tanoi(n-1, start, mid, end) # 맨 아래 거 제외한 애들 중간지점으로 옮김
    print(start, end) # 맨아래 거 도착지점으로 옮김
    tanoi(n-1, mid, end, start) # 중간지점에 있는 애들 도착지점으로 옮김

#tanoi(n, 1, 3, 2)


# DP bottom up이 안되는 이유. 개수가 같다면 걸리는 시간이 같지만 출발지점과 도착지점이 달라서 미리 저장해놀 수 없다?

# 매개변수 2개로 줄일 수 있는 이유? 지점이 1, 2, 3 밖에 없으므로 시작, 도착지점을 아는 상태에서 중간지점은 가능 한게 하나밖에 없기 때문


# 횟수 계산은 bottomup DP로 가능하다.
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    dp[n]= 1+ 2*dp[n-1]
# print(dp[n])
print(2**n-1)
hanoi(n, 1, 3)