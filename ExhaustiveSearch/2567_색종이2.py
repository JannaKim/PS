n= int(input())
mp= [[0]*100 for _ in range(100)]
for _ in range(n):
    a, b= map(int, input().split())
    a, b= b, a
    for i in range(a,a+10):
        for j in range(b, b+10):
            mp[i][j]=1

cnt=0
for i in range(100):
    for j in range(99):
        if mp[i][j]+mp[i][j+1]==1:
            #rint(i, j, i, j+1)
            cnt+=1
            

for i in range(99):
    for j in range(100):
        if mp[i][j]+mp[i+1][j]==1:
            #print(i, j, i+1, j)
            cnt+=1


for i in range(1,99):
    if mp[i][99]:
        cnt+=1
for i in range(1,99):
    if mp[99][i]:
        cnt+=1
if mp[99][99]:
    cnt+=2
#[print(*el) for el in mp]
print(cnt)
