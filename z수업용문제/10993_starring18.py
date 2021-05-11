n= int(input())
r= 1

k=n-1
while k:
    k-=1
    r=2*r+1
c=r*2-1

mp= [[' ']*c for _ in range(r)]

mid= c//2
def rec(lo,hi,dir,dist):
    if lo==hi:
        mp[lo][mid]='*'
        return
    for i in range(r):
        for j in range(c):
            if dir:
                if abs(lo-i)+abs(mid-j)==dist and i>=lo:
                    mp[i][j]='*'
                elif abs(lo-i)+abs(mid-j)<dist and i==lo:
                    mp[i][j]='*'
            else:
                if abs(hi-i)+abs(mid-j)==dist and i<=hi:
                    mp[i][j]='*'
                elif abs(hi-i)+abs(mid-j)<dist and i==hi:
                    mp[i][j]='*'
    if dir:
        rec(lo+1,(lo+hi)//2,not dir,dist//2-1)
    else:
        rec((lo+hi)//2,hi-1,not dir,dist//2-1)

if n%2:
    rec(0,r-1,False,r-1)
else:
    rec(0,r-1,True,r-1)


ends=[]
for i in range(r):
    for j in range(c-1,-1,-1):
        if mp[i][j]=='*':
            ends.append(j)
            break

for i in range(r):
    for j in range(c):
        print(mp[i][j],end='')
        if ends[i]==j:
            break
    print()