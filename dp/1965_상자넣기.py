n = int(input())
L=list(map(int,input().split()))
if n==1:
    print(1)
else:
    #dp[i]:최대 상자개수 수열이 i로 끝날 때
    dp=[1]
    line=[0]
    for i in range(1,n):
        dp.append(1)
        line.append(i)
        for j in range(0,i):
            if L[i]>L[j] and dp[i]<dp[j]+1:
                dp[i] = dp[j]+1
                line[i]=j
            #print(dp)
    '''
    print(f"{'dp':<5}: {dp}")
    print(f"{'index':<5}: {list(range(len(dp)))}")
    print(f"{'line':<5}: {line}")
    print(f"{'L':<5}: {L}")
    '''
    
    #print(max(dp))
    a = dp.index(max(dp))
    p=[]
    while(1):
        p.append(L[a])
        if a!=line[a]:
            a=line[a]
        else:
            break
    print(f"box selected: {p[::-1]}")
'''
8
1 6 2 5 7 3 5 6
'''
