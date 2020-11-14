T = int(input())
P=[0,1,1,1,2,2]
for _ in range(T):
    N = int(input())
    if N<=5:
        print(P[N])
    else:
        a=len(P)
        for i in range(a,N+1):
            P.append(P[i-1]+P[i-5])
        print(P[N])