n=int(input())
garo=(2*n-1)
P=[]

jung=n-1
#도화지= 1*1 3*2 5*3 2n-1*n
#중점=2-1,1 3-2,2
for i in range (n):
    P.append([' ']*garo)
for h in range (n):
    for w in range (garo):
        if abs(h-jung)+abs(w-jung)==jung:
            P[h][w]='*'
for i in range (garo):
    P[jung][i]='*'


y , x = 0 , garo
for i in range(n):
    for j in range(garo):
        if abs(i-y)+abs(j-x)<=jung:
            P[i][j]=''



       
#print(*P,sep='\n')

for el in P:
    print(*el,sep='')