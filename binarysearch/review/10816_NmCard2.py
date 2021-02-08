from typing import ByteString


n= int(input())
L= [*map(int ,input().split())]
L.sort()
m= int(input())
M= [*map(int ,input().split())]

def TP(k):
    lo, hi= 0, n-1
    left=0 #  첫번째 맞는 애 아님 큰애
    while lo<hi:# 어디로 모일까? 같거나 큰애로 모인다
        mid= (lo+hi)//2 # 같거나 큰애가 없을까봐 걱정이다. 그럼 어디가있을까? 작은애한테.
        if L[mid]>=k:
            hi=mid
        else:
            lo=mid+1# 작은애면 저리 치움
    if L[lo]>=k: 
        left=lo
    else:
        left=lo+1
        

    
    lo, hi= 0, n-1
    right=0 #  첫번째 큰애
    while lo<hi:
        mid= (lo+hi)//2 # 큰애가 없을까봐 걱정이다 그럼 어디가있을까? 같거나 작은애한테
        if L[mid]>k:
            hi=mid
        else:
            lo=mid+1
    if L[lo]>k:
        right=lo    
    else:
        right=lo+1
    #print(left, right)
    return right-left
    


ans=[]
#print(L)
for el in M:
    ans.append(TP(el))
print(*ans)

