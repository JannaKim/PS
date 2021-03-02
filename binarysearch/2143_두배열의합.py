t= int(input())
n= int(input())
a= [0]+ [*map(int, input().split())]
m= int(input())
b= [0]+ [*map(int, input().split())]

def getSubSeq(leng, seq, L):
    s=0
    for i in range(1, leng+1):
        s+=seq[i]
        tmp =s
        for j in range(i):
            tmp-=seq[j]
            L.append(tmp)

A=[]
B=[]
getSubSeq(n, a, A)
getSubSeq(m, b, B)
A.sort()
B.sort()

lastB=len(B)-1
def TP(ths):
    global lastB

    # lower bound
    lo= 0
    hi= lastB
    left= 0
    
    while lo<hi: # 같은애들 중 가장 왼쪽, 같은애없으면 큰거중 가장 왼쪽 찾는 게 목표
        mid= (lo+hi)//2
        if B[mid]>=ths:
            hi= mid
        else:
            lo=mid+1
    if B[lo]<ths: # 그런애들이 없었어서 아닌 애를 가리키고 있음
        left=lo+1
    else:
        left=lo


    # upper bound
    lo= 0
    hi= lastB
    right= 0
    
    while lo<hi: # 큰애들 중 가장 왼쪽껄 찾는 게 목표
        mid= (lo+hi)//2
        if B[mid]>ths:
            hi= mid
        else:
            lo=mid+1
    if B[lo]<=ths: # 큰애들이 없었어서 아닌 애를 가리키고 있음
        right=lo+1
    else:
        right=lo

    return right-left
    


ans=0
prv= [1e6+1, 0] # num, ans
for el in A:
    if el==prv[0]:
        ans+=prv[1]
    else:
        prv= [el, TP(t-el)]
        ans+=prv[1]
print(ans)