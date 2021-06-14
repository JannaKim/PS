'''
sum(L[0]) == sum(L[2])
sum(L) = n*(n-1)/2
'''
'''
from itertools import combinations as combi

def valid(H):
        for i in range(6):
            for j in range(i+1 , 6):
                if H[i][j] == H[j][i]:
                    return False
        return True

for _ in range(4):
    inp = [*map(int, input().split())]
    L=[]

    chk = [ [False]*6 for _ in range(6)]

    for i in range(0,18,3):
        L.append(inp[i : i+3])
    #print(*L, sep='\n')
    
    for i in range(6):
        A = list(range(1 , 1+6))
        A.remove(i)

        for ls in combi(A , L[i][0]):
            for country in ls:
                if chk[i][country]:
                H[i][country] = 1
                H[country][i] = 0

  A B C  D E F
A 0 0 0  0 0 0
B 0 0 0  0 0 0
C 0 0 0  0 0 0
D 0 0 0  0 0 0
E 0 0 0  0 0 0
F 0 0 0  0 0 0
'''

def valid(L):
    for i in range(6):
        if sum(L[i]) != 6:
            return 0
    return 1

for _ in range(4):
    inp = [*map(int, input().split())]
    L=[]
    if sum([el[0] for el in L]) != sum([el[2] for el in L]):
        print(0,end=' ')
    elif sum([sum(el) for el in L]) != 30:
        print(0,end=' ')
    elif sum([1 if el[1] else 0 for el in L]) %2:
        print(0,end=' ')
    else:
        print(valid(L),end=' ')

'''
2 * 26
3 ** 17
'''