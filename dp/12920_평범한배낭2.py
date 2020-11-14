N, M = [int(i) for i in input().split()]
wt = [0]
s = [0]

for i in range(N):
    V, C, K = [int(i) for i in input().split()]
    r=0
    if K==1:
        wt.append(V)
        s.append(C)
        continue
    while K > 2**r-1:
        r+=1
    r-=1
    # c <= 2^r-1
    if K==2**r-1:
        for i in range(r):
            wt.append(V*2**i)
            s.append(C*2**i)
    else: 
        #print(f'K={K}, 2**r-1={2**r-1}')
        for i in range(r):
            wt.append(V*2**i)
            s.append(C*2**i)
        
        #print(f'{K-(2**r-1)} 의 2진수: {bin(K-(2**r-1))[2:]}')
        a=0
        for b in bin(K-(2**r-1))[2:][::-1]:
            
            if int(b)*2**r>0:
                wt.append(V*int(b)*2**a)
                s.append(C*int(b)*2**a)
            a+=1
                      
    

#print(wt)
#print(s)


#dp[i][j]: 1~i까지의 물건들중에서 무게j이하로 가져갈때 최대 만족도

dp=[]
for _ in range(len(wt)):
    dp.append([0]*(M+1))


#print(dp)

for i in range(1,len(wt)):
    for j in range(1,M+1):
        if wt[i]<=j:
            dp[i][j] = max(dp[i-1][j-wt[i]] + s[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

#print(dp)

print(dp[len(wt)-1][M])

'''
2 3
2 7 1
1 9 3
'''