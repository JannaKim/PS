#from time import *
N, M, R = map(int, input().split())
mp=[]


mp.append([0]*(M+2))
for _ in range(N):
    mp.append([0]+[int(i) for i in input().split()]+[0])
mp.append([0]*(M+2))
#[print(*i) for i in mp]

chk=[]
chk.append([' ']*(M+2))
for _ in range(N):
    chk.append([' ']+['S']*M+[' '])
chk.append([' ']*(M+2))
#[print(*i) for i in chk]

total=0
def f(i,j,dy,dx,S):
    global total
    #print(i,j, S)

    if mp[i][j]<2 or mp[i+dy][j+dx]==0:
        total+= S
        #print('total=',total)
        return
    _i=i
    _j=j
    go=False
    for idx, K in enumerate(range(1,mp[i][j])):
        if chk[_i+dy][_j+dx]==' ':
            total+=S
            #print('total=',total)
            return

        if chk[_i+dy][_j+dx]=='S':
            if mp[i][j]-1==K:
                go=True
            S+=1
            if idx+1<mp[_i+dy][_j+dx]-1:
                chk[_i+dy][_j+dx]='F'
                #print('새 도미노')
                f(_i+dy,_j+dx,dy,dx, S)
                return

        chk[_i+dy][_j+dx]='F'
        #[print(*i) for i in chk]
        #sleep(0.05)
        _i+=dy
        _j+=dx
    
    if go:
        #print('새 도미노')
        f(_i,_j,dy,dx, S)

    else:
        total+=S
        #print('total=',total)
        return
    

for _ in range(R):
    Ay, Ax, D = input().split()
    Ay=int(Ay)
    Ax=int(Ax)
    Dy, Dx = map(int, input().split())
    #[print(*i) for i in chk]

    if D=='E':
        if chk[Ay][Ax]=='S':
            chk[Ay][Ax]='F'
            #[print(*i) for i in chk]
            f(Ay,Ax,0,1,1)
    elif D=='W':
        if chk[Ay][Ax]=='S':
            chk[Ay][Ax]='F'
            #[print(*i) for i in chk]
            f(Ay,Ax,0,-1,1)
        
    elif D=='S':
        if chk[Ay][Ax]=='S':
            chk[Ay][Ax]='F'
            #[print(*i) for i in chk]
            f(Ay,Ax,1,0,1)
        
    else: #N
        if chk[Ay][Ax]=='S':
            chk[Ay][Ax]='F'
            #[print(*i) for i in chk]
            f(Ay,Ax,-1,0,1)
    chk[Dy][Dx]='S'
    #print('defense',Dy,Dx)
    #[print(*i) for i in chk]
    #print()
        
print(total)
for i in range(1,N+1):
    print(*chk[i][1:M+1])

'''
5 5 3
1 1 1 1 1
1 2 2 1 1
3 1 2 2 2
1 3 2 1 1
1 3 3 1 1
3 1 E
3 5
5 3 N
3 3
5 2 N
3 1
'''


