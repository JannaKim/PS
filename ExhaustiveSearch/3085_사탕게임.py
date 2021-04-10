import sys; input= lambda: sys.stdin.readline().rstrip()

n= int(input())
mp= [list(input()) for _ in range(n)]
ans=-1

def candy_crush(y1, x1,dir):
    mx= 0
    if dir==0: #세로
        
        ths=''.join([el[y1] for el in mp])
        for j in range(n,0,-1):
            if 'C'*j in ths or 'P'*j in ths or 'Z'*j in ths or 'Y'*j in ths:
                mx= max(j,mx)
    
        for i in range(y1, y1+2):
            ths=''.join(mp[i])
            for j in range(n,0,-1):
                if 'C'*j in ths or 'P'*j in ths or 'Z'*j in ths or 'Y'*j in ths:
                    mx= max(j,mx)
                    break

    else: #가로
        for i in range (x1, x1+2):
            ths=''.join([el[i] for el in mp])
            for j in range(n,0,-1):
                if 'C'*j in ths or 'P'*j in ths or 'Z'*j in ths or 'Y'*j in ths:
                    mx= max(j,mx)
                    break 
        ths=''.join(mp[y1])
        for j in range(n,0,-1):
            if 'C'*j in ths or 'P'*j in ths or 'Z'*j in ths or 'Y'*j in ths:
                mx= max(j,mx)
                break
    return mx
            
for i in range(n-1):
    for j in range(n):
        mp[i][j],  mp[i+1][j]= mp[i+1][j], mp[i][j]
        ans= max(ans, candy_crush(i, j, 0))
        mp[i][j],  mp[i+1][j]= mp[i+1][j], mp[i][j]

for i in range(n):
    for j in range(n-1):
        mp[i][j],  mp[i][j+1]= mp[i][j+1], mp[i][j]
        ans= max(ans, candy_crush(i, j,1))
        mp[i][j],  mp[i][j+1]= mp[i][j+1], mp[i][j]

print(ans)