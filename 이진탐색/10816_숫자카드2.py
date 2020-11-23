N = int(input())
L  = [int(i) for i in input().split()]
M = int(input())
*F, = map(int, input().split())
''' 이거 다시하기
def QS(X, first,last):
    if first>=last:
        return
    #print(L)
    #print(first,last)
    p = X[first]
    i = first+1

    j = last
    while i<=j:
        while X[i]<p and i<=last:
            i+=1
        while X[j]>=p and j>first:
            j-=1
        #print(f'i {i} j {j}')
        if i<j:
            X[i], X[j] = X[j], X[i]
            #print('swap',L)
    X[j], X[first] = X[first], X[j]
    #print('pivot',L)
    # j위치에 p 안착
    
    QS(X,first,j-1)
    QS(X,j+1,last)

QS(L,0,N-1)
'''
L.sort()

def lower_bound(L,el): # el보다 작은 값 중 가장 큰값 인덱스 +1
    first = 0
    last = len(L)-1
    idx = last
    while first<last:
        #print(first,last)
        m = (first+last)//2
        if L[m]<el: 
            first = m+1
            idx = m+1
        else: 
            last = m
    if L[first]>=el:
        idx = first
    else:
        idx = first+1
    return idx

# idx 없이 lower bound last 
def upper_bound(L,el):
    first = 0
    last = len(L)-1
    idx = first # 자기보다 큰 요소들중 가장 작은 곳
    while first<last:
        #print(first,last, el)
        m = (first+last)//2
        if L[m]<=el: 
            first = m+1
        else: # 크다면 이 위치 되지만 더 작은곳일 수 있음
            idx = m
            last = m
    if L[first]>el:
        idx = first
    else:
        idx = first+1
    return idx

ans=[]
#print(L)
for el in F:
    lb = lower_bound(L,el)
    ub = upper_bound(L,el)
    #print(lb, ub) # 둘 중 하나만 존재할 수가 없음
    if lb<=len(L)-1 and L[lb]==el and ub>=1 and L[ub-1]==el:
        ans.append(ub-lb)
    else:
        ans.append(0)
    #print('end')
    
print(*ans)




'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
'''