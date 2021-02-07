# 500*500*256 2천..되네..?

n, m, bloc= map(int, input().split())
fie= []
for _ in range(n): fie+=[*map(int, input().split())]

def leveling(hei):
    dig=0
    fill=0
    for acre in fie:
        if acre>hei:
            dig+=2*(acre-hei)
        else:
            fill+=hei-acre

    return (dig, fill)

def BS():
    lo= 0
    hi=256
    while hi-lo>=2:
        m= lo+ (hi-lo)//2
        dig, fill= leveling(m)
        S2= fill
        S1= dig
        B= bloc+S1//2

        if S2>B:
            hi=m-1
        else:
            lo=m
    
    dig, fill= leveling(hi)
    S2= fill
    S1= dig
    B= bloc+S1//2

    if S2<=B:
        return (S1+S2,hi)
    else:
        dig, fill= leveling(lo)
        S2= fill
        S1= dig
        return (S1+S2,lo)


def TS():
    lo= 0
    hi=256
    while hi-lo>=3:
        a= lo+ (hi-lo)//3
        b= lo+ (hi-lo)//3*2
        adig, afill= leveling(a)
        bdig, bfill= leveling(b)


        if adig+ afill> bdig+ bfill:
            lo=a
        elif adig+ afill< bdig+ bfill:
            hi=b
        else:
            lo=a
            hi=b
            print(hi, lo)
    ans=(1e9,0)
    for i in range(lo,hi+1): # 간격 좁힌 세개중에 min 찾기
        dig, fill=leveling(i)
        if fill<=(bloc+(dig//2)) and dig+fill<= ans[0]:
            ans= (dig+fill, i)

    while True: # 같은 값 여러개면 제일 높은 높이로 바꾸기
        dig, fill=leveling(ans[1]+1)
        if fill<=(bloc+(dig//2)) and dig+fill== ans[0]:
            ans[1]+=1
        else:
            break
    return ans
    
m= TS()
k= BS()

if k[1]<=m[1]:
    print(*k)
else:
    print(*m)

'''

7 7 6000
30 21 48 55 1 1 4
0 0 0 0 0 0 0
15 4 4 4 4 4 8
20 40 60 10 20 30 2
1 1 1 1 1 1 9
24 12 33 7 14 25 3
3 3 3 3 3 3 32

Answer : 879 10
'''