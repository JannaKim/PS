from sys import *
input = lambda: stdin.readline().rstrip()
K, N = map(int, input().split())
wire = [int(input()) for _ in range(K)]

def cut(cutter):
    return sum([i//cutter for i in wire])

def BS(a,b):
    #print(a,b)
    m=(a+b)//2
    if b-a<=1:
        if cut(b)>=N:
            return b
        else:
            return a
    if cut(m)>=N:
        return(BS(m,b))
    else:# cut(m)<N:
        return(BS(a,m-1))

print(BS(1,max(wire)))
'''
4 11
802
743
457
539
'''


    