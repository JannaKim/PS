
L=[0]*3
def f(x): # x:2
    L[x]+=1
    print(*L)
    if x<2:
        f(x+1)
    L[x]-=1
    if x<2:
        f(x+1)
f(0)
