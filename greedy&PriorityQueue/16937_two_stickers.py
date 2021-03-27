import sys; input= lambda: sys.stdin.readline().rstrip(); r=range
h, w= map(int, input().split())
n= int(input())
stic= []
for _ in r(n):
    a, b= map(int,input().split())
    stic.append((a, b))

ans= 0
for i in r(n-1):
    for j in r(i+1, n):
        ah, aw= stic[i]
        bh, bw= stic[j]
        for _ in range(2):
            for __ in range(2):
                if max(ah,bh)<=h and aw+bw<= w:
                    ans= max(ans, ah*aw+ bh*bw)
                if ah+bh<=h and max(aw,bw)<=w:
                    ans= max(ans, ah*aw+ bh*bw)
                bh, bw= bw, bh
            ah, aw= aw, ah
print(ans)

'''
MIS = lambda: map(int,input().split())

def poss_unit(a1, b1, a2, b2):
    # horizontal a, vertical b
    if b1+b2 <= h: return a1 <= w and a2 <= w
    if a1+a2 <= w: return b1 <= h and b2 <= h
    return False

def poss(a1, b1, a2, b2):
    for (a,b) in (a1,b1), (b1,a1):
        for (c,d) in (a2,b2), (b2,a2):
            if poss_unit(a,b,c,d): return a*b+c*d
    return 0

h, w = MIS()
n = int(input())
if n < 2: print(0); exit()
stic = [tuple(MIS()) for i in range(n)]
print(max(poss(*stic[i], *stic[j]) for i in range(n) for j in range(i+1, n)))
'''


'''
import sys; input= lambda: sys.stdin.readline().rstrip(); r=range
h, w= map(int, input().split())
n= int(input())
stic= []
for _ in r(n):
    a, b= map(int,input().split())
    stic.append((a, b))

ans= 0
for i in r(n-1):
    for j in r(i+1, n):
        ah, aw= stic[i]
        bh, bw= stic[j]
        
        if max(ah,bh)<=h and aw+bw<= w:
            ans= max(ans, ah*aw+ bh*bw)
        if ah+bh<=h and max(aw,bw)<=w:
            ans= max(ans, ah*aw+ bh*bw)

        bh, bw= bw, bh
        if max(ah,bh)<=h and aw+bw<= w:
            ans= max(ans, ah*aw+ bh*bw)
        if ah+bh<=h and max(aw,bw)<=w:
            ans= max(ans, ah*aw+ bh*bw)

        ah, aw= aw, ah
        if max(ah,bh)<=h and aw+bw<= w:
            ans= max(ans, ah*aw+ bh*bw)
        if ah+bh<=h and max(aw,bw)<=w:
            ans= max(ans, ah*aw+ bh*bw)

        bh, bw= bw, bh
        if max(ah,bh)<=h and aw+bw<= w:
            ans= max(ans, ah*aw+ bh*bw)
        if ah+bh<=h and max(aw,bw)<=w:
            ans= max(ans, ah*aw+ bh*bw)
print(ans)


'''