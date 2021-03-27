f, s, g, u, d= map(int, input().split())
'''
g: goal
f: final floor
s: start Floor
'''
if s>g:
    s,g= g,s
    u,d= d,u


# 위로 올라가야함
if u==0:
    quo=(g-s)
else:
    quo= (g-s)//u
if s+u*quo==g:
    print(quo)
else:
    loc=s+u*(quo+1)
    if loc==s: # 미동도 안함
        print('use the stairs')
        exit()
    # 아래로 내려가야함
    quo2= (loc-g)//d
    if loc-d*quo2==g:
        print((quo+1)+quo2)
    else:
        print('use the stairs')