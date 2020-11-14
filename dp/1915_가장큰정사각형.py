#chk[i][j] = a, a: i,j를 오른쪽아래 꼭짓점으로 하는 가장 큰 정사각형의 변

n, m = map(int, input().split()) # 세로, 가로

mp = []
mp.append([0]*(m+2))
for _ in range(n):
    mp.append([0]+list(map(int,list(input())))+ [0])
mp.append([0]*(m+2))

chk = []

for _ in range(n+2):
    chk.append([0]*(m+2))
#[print(*i) for i in mp]
print()

'''
4 4
0111
0111
1111
0111
'''
mx = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        if mp[i][j]==1:
            chk[i][j] = min(chk[i-1][j],chk[i][j-1],chk[i-1][j-1])+1
            mx = max(mx, chk[i][j])
#[print(*i) for i in chk]
print(int(mx*mx))


