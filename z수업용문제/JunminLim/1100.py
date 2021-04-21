x=[]

ans=0
for i in range (4):
    x+=[[0,1,0,1,0,1,0,1]]
    x+=[[1,0,1,0,1,0,1,0]]


y=[]
for _ in range(8):
    y.append(input())

for i in range (8):
    for j in range (8):
        if x[i][j]==0 and y[i][j]=='F':
            ans+=1
print(ans)