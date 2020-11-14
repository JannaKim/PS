N = int(input())
cnslt=[[0,0]]
for _ in range(N):
    cnslt.append([int(i) for i in input().split()])

# dp[i][0]: i일전까지 일했을 때 얻을 수 있는 최대 수익
# dp[i][1]: 최대수익의 시작일

dp=[[0,0]]*(N+1) # 2차원 배열을 이렇게 생성하면 같은 주소를 공유하게 된다..!
L=[0]*(N+1)
for i in range(1,N+1):
        L[i] = cnslt[i][1]
print(L,'\n')
print(dp)
for i in range(1,N+1):
    if i+cnslt[i][0]<=N:
        print(f"추가중 dp[{i+cnslt[i][0]}][0]")
        dp[i+cnslt[i][0]][0]=max(dp[i+cnslt[i][0]][0], dp[i][0]+cnslt[i][1])
        print(dp,'?')
        print(f"dp[{i+cnslt[i][0]}][0],{dp[i][0]}+cnslt[i][1]")
        if dp[i+cnslt[i][0]][0] < dp[i][0]+cnslt[i][1]:
            print(1)
            dp[i+cnslt[i][0]][1]= dp[i][1]
        print(dp)



'''
for i in range(1,N+1):
    if i+cnslt[i][0]<=7:
        dp[i]+=cnslt[i][1]
print(dp)
print(max(dp))
'''
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
4
1 1
3 1
1 1
1 1
'''
'''
seq=[]
for i in range(1,N+1):
    print(f'{i}+{cnslt[i][0]}')
    if i+cnslt[i][0]<=N:
        print(f'->   {i}+{cnslt[i][0]}')
        seq.append(i+cnslt[i][0])
        seq.append(i)
print(seq)
seq.sort()

for i in seq:
        #print(f'dp[{a}]=max(dp[{a}], dp[{b}]+{c})')
        #seq.append([i+cnslt[i][0],i,cnslt[i][1]])
        if i-cnslt[i][0]>0 and i+cnslt[i-cnslt[i][0]][0]<=N:
            print(f"max(dp[{i}+cnslt[{i-cnslt[i][0]}][0]], dp[{i-cnslt[i][0]}]+cnslt[{i-cnslt[i][0]}][1])")
            dp[i]=max(dp[i+cnslt[i-cnslt[i][0]][0]], dp[i-cnslt[i][0]]+cnslt[i-cnslt[i][0]][1])
        
            print(dp,'\n')
'''