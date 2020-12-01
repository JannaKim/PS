#L = [1 ,5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

def median(A):
    if len(A)==5:
        R=[0]*3 # round
        R[0]= (0 if A[0]>A[1] else 1)
        R[1]= (2 if A[2]>A[3] else 3)
        R[2] = (R[0] if A[R[0]]>A[R[1]] else R[1]) # A[0:5] 중 winner의 index
        
        A[R[2]]=A[4] # 그 winner 빼고 그 자리에 L[4]넣는다

        if not R[2]%2: # 왼쪽
            R[R[2]//2]= (R[2] if A[R[2]]>A[R[2]+1] else R[2]+1)
        else: # 오른쪽
            R[R[2]//2]= (R[2] if A[R[2]]>A[R[2]-1] else R[2]-1)

        if A[R[0]]>A[R[1]]: # winner 제외 나머지 셋 중 max
            return max(A[R[0]^1], A[R[1]])
        else:
            return max(A[5-R[1]], A[R[0]])
    elif len(A)==4:
        R=[0]*2
        R[0]= (0 if A[0]>A[1] else 1)
        R[1]= (2 if A[2]>A[3] else 3)
        return A[R[0]] if A[R[0]]<A[R[1]] else A[R[1]]
    elif len(A)==3:
        if A[0]< A[1]:
            if A[1]<A[2]:
                return A[1]
            elif A[2]<A[0]:
                return A[0]
            else:
                return A[2]
        else: # A[1]<=A[0]
            if A[2]<A[1]:
                return A[1]
            elif A[0]<A[2]:
                return A[0]
            else:
                return A[2]
    else:
        return A[0]

print(median([1,5,3,4]))