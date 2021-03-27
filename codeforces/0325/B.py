import sys; input= lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n, k= map(int, input().split())
    s= input()
    first=0
    last=n-1
    S=[]
    for el in s:
        if el=='.':
            S.append(0)
        else:
            S.append(1)

    for idx, el in enumerate(S):
        if el==1:
            first=idx
            break
    for i in range(n-1,-1,-1):
        if S[i]==1:
            last=i
            break

    S[first]=2
    S[last]=2

    here=first
    cnt=2
    if first==last:
        cnt-=1
    done=False
    while not done:
        here= min(here,n-k-1)
        for i in range(here+k,here-1,-1):
            if S[i]==1:
                here=i
                S[i]=2
                cnt+=1
                break
            elif S[i]==2:
                done=True
                break
    print(cnt)

