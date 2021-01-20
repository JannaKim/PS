
int R[3];
int median(int a, int b){
    if(b-a+1==5)
    {
        A[a+0]>A[a+1] ? R[0]=0 : R[0]=1;
        A[a+2]>A[a+3] ? R[1]= 2 : R[1]=3;
        A[a+R[0]]>A[a+R[1]] ? R[2]=R[a+0] : R[2]=R[1]; // A[0:5] 중 winner의 index
        
        A[R[a+2]]=A[4]; // 그 winner 빼고 그 자리에 L[4]넣는다

        if(R[2]%2==1) // 왼쪽
            (A[a+R[2]]>A[a+R[2]+1])? R[R[2]>>1]= R[2] : R[R[2]>>1]=R[2]+1;
        else (A[a+R[2]]>A[a+R[2]-1])? R[R[2]>>1]= R[2] : R[R[2]>>1]= R[2]-1;

        if(a+A[R[0]]>A[a+R[1]])// # winner 제외 나머지 셋 중 max
            return max(A[a+R[0]^1], A[a+R[1]]);
        else
            return max(A[a+5-R[1]], A[a+R[0]]);
    }
    else if(b-a+1==4)
    {
        (A[a+0]>A[a+1]) ? R[0]= 0: R[0]= 1;
        (A[a+2]>A[a+3]) ? R[1]= 2: R[1]= 3;
        int ans;
        (A[R[0]]<A[R[1]])? ans= A[R[0]] : ans= A[R[1]];
    }
    else if(b-a+1==3)
    {
        if(A[a+0]< A[a+1])
        {
            if(A[1]<A[2])
                return A[a+1];
            else if(A[2]<A[0])
                return A[a+0];
            else:
                return A[2]
        }
        else: # A[1]<=A[0]
            if A[2]<A[1]:
                return A[1]
            elif A[0]<A[2]:
                return A[0]
            else:
                return A[2]
    }
    else:
        return A[0]
}

def MoM(L):
	if len(L) == 1: # no more recursion
		return L[0]
	medians=[]
	for i in range(0,len(L),5):
		medians.append(median(L[i: min(i+5,len(L))]))

	mom = MoM(medians)
	return mom