n, m= map(int, input().split())

castle=[]
for _ in range(n):
    castle.append(list(input()))

cnt=0
for i in range(n):
    if sum(list(map(ord,castle[i])))==4*46:
        flag=True
        for j in range(n):
            if sum([ord(castle[k][j]) for k in range(4)])==4*46:
                flag=False
                castle[i][j]='X'
                cnt+=1
                break
        if flag:
            castle[i][0]='X'
            cnt+=1

new=[['.']*n for _ in range(m)]
for i in range(n):
    for j in range(m):
        new[n-j+1][i]=castle[i][j]

[print(*el) for el in new]
print(cnt)
print(ord('.'))

                    