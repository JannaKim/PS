import sys; input= lambda: sys.stdin.readline().strip();r= range
n, m= map(int, input().split())

mp= [[-1]*(m+2)]
mp+=[[-1]+[*map(int,input().split())]+[-1] for _ in range(n)]
mp+= [[-1]*(m+2)]

origin= [[-1]*(m+2) for _ in range(n+2)]
for i in range(1,n+1):
    for j in range(1, m+1):
        origin[i][j]=mp[i][j]

mx=0
dy= [0, 0, 1, -1]
dx= [1, -1, 0, 0]
Ay= [-1, -1, -1, 0, 0, 1, 1, 1]
Ax= [-1, 0, 1, -1, 1, -1, 0, 1]

def spread(i, j):
    for y, x in zip(dy, dx):
        if mp[i+y][j+x]==0: # spreadable
            mp[i+y][j+x]=3
            spread(i+y, j+x)

def test(): # spread virus
    for i in r(1, n+1):
        for j in r(1, m+1):
            if mp[i][j]==2:
                spread(i, j)
    return safeplace()
    

def safeplace():
    cnt=0
    for i in r(1, n+1):
        for j in r(1, m+1):
            if not mp[i][j]:
                cnt+=1
    return cnt


def isValid(i,j): # 이거 안됨. 대각선 바리케이트 치는게 최선일 수가 있음
    valid=False
    for y, x in zip(Ay, Ax): # diagonal?
        if mp[i+y][j+x]>0:
            valid=True
            break
    return valid


def backtrack(i, j, isSet):
    global mx
    if isSet==0:
        tmp=test()
        mx=max(mx, tmp)
        for i in range(1,n+1):
            for j in range(1, m+1):  # 고른것도 지워버리는 오리진;
                mp[i][j]= origin[i][j]
        return

    if i>n: return
    if mp[i][j]==0:# and isValid(i, j):
        mp[i][j]=1
        origin[i][j]=1
        if j==m:
            backtrack(i+1, 1, isSet-1)
        else:
            backtrack(i, j+1, isSet-1)
        mp[i][j]=0
        origin[i][j]=0
    if j==m:
        backtrack(i+1, 1, isSet)
    else:
        backtrack(i, j+1, isSet)

backtrack(1, 1, 3)
print(mx)



'''
o,b,a=[],[],0
N,M=map(int,input().split())
for r in range(N):o+=list(map(int,input().split()))
for i in range(N*M):
	if o[i]==0:b+=[i]
h=len(b)
for i in range(h-2):
	for j in range(i+1,h):
		for k in range(j+1,h):
			m,q=o[:],[]
			m[b[i]],m[b[j]],m[b[k]]=1,1,1
			for v in range(N*M):
				if m[v]==2:q+=[v]
			for v in q:
				if m[v]==2:
					U,R,D,L=v-M,v+1,v+M,v-1
					if m[U]==0and U>=0:m[U]=2;q+=[U]
					if R<N*M and m[R]==0and R%M:m[R]=2;q+=[R]
					if D<N*M and m[D]==0:m[D]=2;q+=[D]
					if m[L]==0and L%M!=M-1:m[L]=2;q+=[L]
			s=m.count(0)
			if a<s:a=s
print(a)
'''