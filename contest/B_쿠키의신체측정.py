N = int(input())
mp = []
mp.append(['_']*(N+2))
for _ in range(N):
    mp.append(['_']+list(input())+['_'])
mp.append(['_']*(N+2))

#[print(*i) for i in mp]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
heart =[]
found=False
for i in range(1,N+1):
    if found==True:
        break
    for j in range(1,N+1):
        if mp[i][j]=='*':
            cnt=0
            for x,y in zip(dx,dy):
                if mp[i+x][j+y]=='*':
                    cnt+=1
            if cnt==4:
                heart = (i,j)
                found=True
                break
body = [0,0,0,0,0] # l arm, r arm, waist, l leg, r leg 

# l arm
for i in range(heart[1]-1, 0,-1):
    if mp[heart[0]][i]=='*':
        body[0]+=1
    else:
        break


# right arm

for i in range(heart[1]+1, N+1):
    if mp[heart[0]][i]=='*':
        body[1]+=1
    else:
        break

# waist
waist_end=0
for i in range(heart[0]+1, N+1):
    if mp[i][heart[1]]=='*':
        body[2]+=1
    else:
        waist_end=(i,heart[1])
        break

# left leg
for i in range(waist_end[0], N+1):
    if mp[i][waist_end[1]-1]=='*':
        body[3]+=1
    else:
        break

# right leg
for i in range(waist_end[0], N+1):
    if mp[i][waist_end[1]+1]=='*':
        body[4]+=1
    else:
        break


print(*heart)
print(*body)
            



'''
5
_____
_*___
*****
_*___
*_*__
'''