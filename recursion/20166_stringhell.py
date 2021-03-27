import sys; input= lambda: sys.stdin.readline().rstrip()

n, m, k= map(int, input().split())
mp=[list(input()) for _ in range(n)]
ans=0
DY=[0,0,1,1,1,-1,-1,-1]
DX=[1,-1,0,1,-1,0,1,-1]
def rec(y, x, idx,tot,s):
    global n
    if idx==tot:
        global ans
        ans+=1
        return
    for dy, dx in zip(DY, DX):
        ny=(y+dy+n)%n
        nx=(x+dx+m)%m
        if mp[ny][nx]==s[idx]:
            rec(ny, nx, idx+1,tot,s)
L=[]
dic={}
for _ in range(k):
    tmp=input()
    L.append(tmp)
    dic[tmp]=0

ques=sorted(L)
start=0
#print(ques)
for idx,(a, b) in enumerate(zip(ques,ques[1:])):
    if a[0]!=b[0]:     
        for i in range(n):
            for j in range(m):
                if mp[i][j]==a[0]:                
                    for t in range(start,idx+1):
                        ans=0
                        rec(i, j, 1,len(ques[t]),ques[t])
                        dic[ques[t]]+=ans
        start=idx+1
for i in range(n):
    for j in range(m):
        if mp[i][j]==ques[-1][0]: 
            for t in range(start,k):
                ans=0
                rec(i, j, 1,len(ques[t]),ques[t])
                dic[ques[t]]+=ans
for el in L:
    print(dic[el])