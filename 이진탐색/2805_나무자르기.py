N, M = map(int, input().split())
*tree, = map(int, input().split())

def cut(cutter):
    return sum([i-cutter for i in tree if i>cutter])

def BS(a,b):
    m = (a+b)//2
    if (b-a)<=1:
        if cut(b)>=M:
            return b
        else:
            return a
    elif cut(m)<M:
        return BS(a,m-1)
    elif cut(m)>M:
        return BS(m,b)
    else:
        return m


print(BS(0,int(1e9))) # 바닥에서 자르는 것도 되겠지..
'''
4 7
20 15 10 17
'''