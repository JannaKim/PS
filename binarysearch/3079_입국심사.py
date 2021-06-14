# 10:36 - 10:49 WA
n , m = map(int, input().split())
T = [int(input()) for _ in range(n)]

def test(k):
    sm = 0
    for el in T:
        sm += ( k // el )
    #print(sm , m)
    if sm >= m:
        return True
    return False

lo = 0
hi = int(1e18)
ans = -1
while lo < hi:
    mid = (lo + hi) # 2  34 35
    if test(mid):
        hi = mid
    else:
        lo = mid + 1
        ans = mid + 1
print(ans)