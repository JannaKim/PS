n, m= map(int, input().split())

castle=[]
for i in range(n):
    castle.append([])
    for idx, el in enumerate(input()):
        if el=='.':
            castle[i].append(0)
        else:
            castle[i].append(1)

cnt=0
for i in range(n):
    if sum(castle[i])==0:
        #print(i)
        for j in range(m): # 열별로 검사
            flag=True
            for k in range(n):
                #print(k, j)
                if castle[k][j]==1:
                    flag=False
                    #print('1 found')
                    break
            if flag:
                castle[i][j]=1
                #[print(*el) for el in castle]
                cnt+=1
                break
            if j==m-1 and not flag:
                castle[k][j]=1
                cnt+=1

scnd= [[0]*n for _ in range(m)]

for i in range(n):
    for j in range(m):
        scnd[j][n-1-i] = castle[i][j]
#[print(*el) for el in castle]
#print(cnt)
for i in range(m):
    if sum(scnd[i])==0:
        #print(i)
        for j in range(n): # 열별로 검사
            flag=True
            for k in range(m):
                #print(k, j)
                if scnd[k][j]==1:
                    flag=False
                    #print('1 found')
                    break
            if flag:
                scnd[i][j]=1
                #[print(*el) for el in castle]
                cnt+=1
                break
            if j==n-1 and not flag:
                scnd[k][j]=1
                cnt+=1
#[print(*el) for el in scnd]
#[print(*el) for el in castle]
print(cnt)