'''
점 a,b를 c,d기준 90도 회전
(c+d-b, d+c-a)

끝점은 시작점을 어떤기준으로 rotate한 것
'''
'''
a, b, c, d=(map(int, input().split()))


print(c+b-d, d+c-a)
'''
def rotate(axis, standard):
    a, b= axis
    c, d= standard
    return (c+b-d, d+c-a)

mp= [[0]*101 for _ in range(101)]
n= int(input())
dy=[0,-1,0,1]
dx=[1,0,-1,0]
for _ in range(n):
    dragon=[]
    x, y, d, g= map(int, input().split())
    mp[y][x]=1
    #print(y,x)
    dragon.append((y,x))
    dragon.append((y+dy[d], x+dx[d]))
    mp[y+dy[d]][x+dx[d]]=1
    #print(y+dy[d],x+dx[d])
    end= (y+dy[d], x+dx[d])
    #print(f'end {end}')
    for _ in range(g):
        st= end
        end= rotate((y, x), end)
        
        #print(f'end {end}')
        mp[end[0]][end[1]]=1
        
        #print(tuple(end), 'rotate',(y,x), st)
        newdragon=[]
        for i, j in dragon:
            r, c= rotate((i,j), st)
            mp[r][c]=1
            #print(r,c, 'rotate',(i,j), st)
            newdragon.append((r,c))
        dragon.append(st)
        dragon+=newdragon
    #print('done')
        
        #[print(*el) for el in mp]
ans=0
for i in range(100):
    for j in range(100):
        #print(i+1,j+1)
        if mp[i][j]:
            if mp[i+1][j] and mp[i][j+1] and mp[i+1][j+1]:
                ans+=1

print(ans)

#[print(*el[:5]) for el in mp[:10]]

