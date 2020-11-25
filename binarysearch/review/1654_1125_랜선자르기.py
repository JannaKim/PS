K, N = map(int, input().split())
wire = [int(input()) for _ in range(K)]

def cut(C):
    s= 0
    for i in range(K):
        s+= wire[i]//C
    return s

def bs(first, last):
    if last-first<=1:
        if cut(last)>=N:
            return last
        else:
            return first
    m = (first+last)//2
    if cut(m)<N:
        return bs(first,m-1)
    else:
        return bs(m,last)

print(bs(1,int('1'*31,2)))

'''
4 11
802
743
457
539
'''