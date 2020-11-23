N = int(input())
*card, = map(int, input().split())
M = int(input())
*find, = map(int, input().split())

def merge(L,first,last):
    i = first
    m = (first+last)//2
    j = m+1
    A = []
    while i<=m and j<=last:
        if L[i]<=L[j]:
            A.append(L[i])
            i+=1
        else:
            A.append(L[j])
            j+=1
    for k in range(i,m+1):
        A.append(L[k])
    for k in range(j,last+1):
        A.append(L[k])
    for i in range(first,last+1):
        L[i] = A[i-first]

def MS(L,first,last):
    if first>=last:
        return 
    m = (first+last)//2
    MS(L,first,m) # 작은애들부터 순서정하고 큰거 계산하도록 계속재귀
    MS(L,m+1,last) # 잘게 쪼개서
    #print(f'merge도착, {first},{last}')
    merge(L,first,last)# 작은것부터 합침

MS(card,0,N-1) # sort

def BS(card, el,a, b):
    if a>=b:
        if card[a]==el:
            return 1
        else:
            return 0    
    else:
        m = (a+b)//2
        if el<card[m]:
            return BS(card,el,a,m-1)
        elif el>card[m]:
            return BS(card,el,m+1,b)
        else:
            return 1

ans=[]
for el in find:
    ans.append(BS(card,el, 0, N-1))
print(*ans)

'''
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
'''


