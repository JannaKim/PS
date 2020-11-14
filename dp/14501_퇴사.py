N = int(input())
cnslt=[[0,0]]
for _ in range(N):
    cnslt.append([int(i) for i in input().split()])

# dp[i]: i일'전'까지 받을 수 있는 최대 수익
dp=[0]*(N+1)
L=[0]*(N+1)
for i in range(1,N+1):
        L[i] = cnslt[i][1]
#print(L)
for i in range(1,N+1):
    #print(f"dp[{i}]")
    for j in range(1,i):
        if j+cnslt[j][0]==i:
            #print(f"{j}일 꺼 더함")
            dp[i] = max(dp[i],dp[j]+cnslt[j][1])
        #print(dp)

print(dp)      
# dp[i]: i일'까지'까지 일할 수 있을 때 받을 수 있는 최대 수익
for i in range(N+1):
    if i+cnslt[i][0]<=7:
        dp[i]+=cnslt[i][1]
    
print(dp)
print(max(dp))

'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''

'''
if i+cnslt[i][0]<8:
        a = 0
        if cnslt[i+cnslt[i][0]][0]==1:
            a=cnslt[i+cnslt[i][0]][1]
        print(f"max(dp[{i+cnslt[i][0]}], dp[{i}]+{a})")
        dp[i+cnslt[i][0]]=max(dp[i+cnslt[i][0]], dp[i]+a)
'''