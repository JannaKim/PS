N = int(input())
L  = [int(i) for i in input().split()]
M = int(input())
*F, = map(int, input().split())
'''
위의 정렬 방식은 간단하면서도 재귀함수를 사용하는 방식의 문제풀이 방법이다, 하지만 입력이 커지면 커질수록 피벗값보다 작은 리스트, 같은 리스트, 큰 리스트들을 만들고 그 리스트들 안에서 또 작고 큰 리스트를 생성해야 하기 때문에 메모리의 비효율 성을 낳게 됩니다. 그러므로 메모리를 적게 사용하는 inplace 형식의 sort방법을 알아봅시다.
'''
def QS(X, a,b):
    if a>=b:
        return

    p = X[a]
    i = a+1
    j = b
    while i<=j:
        while i<=b and X[i]<=p:
            i+=1
        while X[j]>p:
            j-=1
        if i<j:
            X[i], X[j] = X[j], X[i]
            i+=1
            j-=1

    X[j], X[a] = X[a], X[j]

    
    QS(X,a,j-1)
    QS(X,i,b)
'''

def QS(A, first, last):
    if first>=last:
        return

    p = L[(first+last)//2]
    i = first
    j = last

    while i<=j:
        while L[i]<p:
            i+=1
        while L[j]>p:
            j-=1
        if i<=j:
            L[i], L[j] = L[j], L[i]
            i+=1
            j-=1
    QS(L,first,j)
    QS(L,i,last)
    


'''

QS(L,0,N-1)


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