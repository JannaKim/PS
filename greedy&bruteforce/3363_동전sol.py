coin=[[] for _ in range(3)]
result=[' ']*3
for i in range(3):
    s = input().split()
    result[i]=s[4]
    del s[4]
    coin[i]=tuple(map(int, s))


info = [[['=']*3 for _ in range(2)] for _ in range(13)]
for i in range(3): 
    for j in range(4):
        c = coin[i][j]
        info[c][0][i]='<'
        info[c][1][i]='>'
        [print(info[i][0], end=' ') for i in range(1,13)]
        print()
        [print(info[i][1], end=' ') for i in range(1,13)]
        print()
        print()
    for j in range(4,8):
        c = coin[i][j]
        info[c][0][i]='>'
        info[c][1][i]='<'
        [print(info[i][0], end=' ') for i in range(1,13)]
        print()
        [print(info[i][1], end=' ') for i in range(1,13)]
        print()
        print()

sol=0
fls = -1
sgn = ' '

for coin in range(1,13):
    if info[coin][0]==result:
        sol+=1
        fls = str(coin)
        sgn='-'
    if info[coin][1]==result:
        sol+=1
        fls = str(coin)
        sgn='+'

if sol==0: print("impossible")
elif sol==1: print(fls+sgn)
else: print("indefinite")
