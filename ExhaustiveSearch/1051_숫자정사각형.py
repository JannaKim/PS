n , m = map(int , input().split())
mp = [input() for _ in range(n)]

def chk(*loc):
    for y , x in loc:
        if  y < 0 or y >= n or x < 0 or x >= m:
            return False
    return True

ans = 0
def isSame(a , b , c , d , e , f , g , h):
    if not chk((a,  b) , (c , d) , (e , f) , (g , h )):
        return False
    if mp[a][b] == mp[c][d]:
        if mp[a][b] == mp[e][f]:
            if mp[a][b] == mp[g][h]:
                return True
    return False
for side in range(min(n , m)):
    for i in range(n):
        for j in range(m):
            if isSame(i , j , i + side , j , i , side + j , i + side , j + side ):
                ans = max(ans , side + 1)

print(ans ** 2)