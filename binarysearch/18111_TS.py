import sys; input= lambda: sys.stdin.readline().strip()
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

def TS():
    lo= 0
    hi=max(fie)
    while hi-lo>=3:
        a= lo+ (hi-lo)//3
        b= lo+ (hi-lo)//3*2
        adig, afill= leveling(a)
        bdig, bfill= leveling(b)

        if afill>(bloc+(adig//2)): # inventory chk
            hi=a-1
            continue
        elif bfill>(bloc+(bdig//2)):
            hi=b-1
            continue

        if adig+ afill>= bdig+ bfill:
            lo=a
        elif adig+ afill< bdig+ bfill:
            hi=b
    ans=(1e9,0)
    for i in range(lo,hi+1): # find min of remains
        dig, fill=leveling(i)
        if fill<=(bloc+(dig//2)) and dig+fill<= ans[0]:
            ans= (dig+fill, i)

    return ans
print(*TS())


L= [1, 2, 3, 4]
'''
1. 강단조증가
2. 교차가 min?
3. x 경우 때문에 lo 만 조정
'''
