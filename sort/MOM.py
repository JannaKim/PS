def find_median_five(L):
    if len(L)==5:
        R=[0]*3
        R[0] = (0 if L[0]>=L[1] else 1)
        R[1] = (2 if L[2]>=L[3] else 3)
        R[2] = (R[0] if L[R[0]]>=L[R[1]] else R[1])
        L[R[2]]=L[4]

        if not R[2]%2: #왼쪽
            R[R[2]//2] = (R[2] if L[R[2]]>= L[R[2]+1] else R[2]+1)
        else:
            R[R[2]//2] = (R[2] if L[R[2]]>= L[R[2]-1] else R[2]-1)
            R[2] = (R[0] if L[R[0]]>=L[R[1]] else R[1])
        
        # 2등까지 결정됨.

        if L[R[0]]>L[R[1]]: # winner 제외 나머지 셋 중 max
            return max(L[R[0]^1], L[R[1]])
        else:
            return max(L[5-R[1]], L[R[0]])

    elif len(L)==4:
        R=[0]*3
        R[0]=(0 if L[0]>=L[1] else 1)
        R[1]=(2 if L[2]>=L[3] else 3)
        if L[R[0]]>=L[R[1]]:
            return L[R[1]]
        else:
            return L[R[0]]
    elif len(L)==3:
        if L[0]<=L[1]:
            if L[1]<=L[2]:
                return L[1]
            elif L[2]<=L[0]:
                return L[0]
            else:
                return L[2]
        else: # L[i+1]<L[i]
            if L[0]<=L[2]:
                return L[0]
            elif L[2]<=L[1]:
                return L[1]
            else:
                return L[2]
    else:
        return L[0]


	
def MoM(L, k): # L의 값 중에서 k번째로 작은 수 리턴
	if len(L) == 1: # no more recursion
		return L[0]
	A, B, M, medians = [], [], [], []
	for i in range(0,len(L),5):
		medians.append(find_median_five(L[i: min(i+5,len(L))]))

	mom = MoM(medians,len(medians)//2)

	for v in L:
		if v<mom: A.append(v)
		elif v>mom: B.append(v)
		else: M.append(v)

	if len(A)>=k: return MoM(A,k)2
	elif len(A)+len(M)<k: return MoM(B,k-len(A)-len(M))
	else: return mom


# n과 k를 입력의 첫 줄에서 읽어들인다
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)

n, k = map(int, input().split())
L=[int(i) for i in input().split()]
print(MoM(L, k))