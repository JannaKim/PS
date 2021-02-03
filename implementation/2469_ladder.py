import sys; input= lambda: sys.stdin.readline().rstrip()
k= int(input())
length= int(input())
players= input()

ladder= [input() for _ in range(length)]

up=[chr(65+i) for i in range(k)]


for line in ladder: 
    if line[0]=='?':
        break
    for idx, col in enumerate(line):
        if col=='-':
            up[idx], up[idx+1]= up[idx+1], up[idx]
            

down= list(players)
for line in ladder[::-1]:
    if line[0]=='?':
        break
    for idx, col in enumerate(line):
        if col=='-':
            down[idx], down[idx+1]= down[idx+1], down[idx]

ans=[]
for i, (u, nu, d, du) in enumerate(zip(up,up[1:], down,down[1:])): # 붙이는거조심 길이 안늘려야하는구나
    if u==du and nu==d:
        ans.append('-')
        down[i], down[i+1]= down[i+1], down[i]
    else:
        ans.append('*')

print([''.join(ans),'x'*(k-1)][up!=down])



t=[*range(int(input()))]
l=int(input())
o=[ord(i)-65 for i in input()]
def g(l,s):
    for i,v in enumerate(s):
        if v=='-':l[i],l[i+1]=l[i+1],l[i]
for i in range(l):
    s=input()
    if s[0]=='?':break
    g(t,s)
for s in [input() for _ in range(l-i-1)][::-1]:g(o,s)
v=lambda i,j=0,k=0:t[i+j]==o[i+k]
n=len(t)-1
s=''.join('*-'[v(i,0,1) and v(i,1,0)]for i in range(n))
g(t,s)
print(['x'*n,s][t==o])