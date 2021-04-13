def solution(N, stages):
    tot= len(stages)
    ing= [0]*(502) #################
    for num in stages:
        ing[num]+=1
    
    dp=[0]*(N+1)
    sum=0
    for i in range(1,N+1):
        sum+=ing[i-1]
        dp[i]=tot-sum
    #print(dp)
    q=[]
    for i in range(1,N+1):
        ths=1
        if dp[i]>0:
            if ing[i]>0:
                ths=1-ing[i]/dp[i]
        q.append((ths,i))
    #print(sorted(q))
    answer=list(map(lambda x:x[1], sorted(q)))

    return answer

print(solution(	5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(	1, [1,1,1]))
#print(solution(	6, [2, 2, 2, 6, 2, 4, 3, 3]))
#print(float(199999)/200000)