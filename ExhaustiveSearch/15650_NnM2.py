n, m= map(int, input().split())
chk=[False]*(n+1)
def choose(i, cnt):
    #print('cur',i, cnt)
    if not cnt:
        for j in range(1,n+1):
            if chk[j]:
                print(j, end=' ')
        print()
        return
    if i==n+1:
        return
    for j in range(i,n+1):
        if not chk[j]:
            #print(f'choose {j}')
            chk[j]=True
            choose(j+1, cnt-1)
            #print(f'unchoose {j}')
            chk[j]=False

choose(1,m)