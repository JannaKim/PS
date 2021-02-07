import time
n, s= map(int, input().split())
L= [*map(int, input().split())]

DP= [[1]+[0]*100000*20 for _ in range(n)]
NP= [[0]*(100000*20+1) for _ in range(n)]
if L[0]<0:
    NP[0][-L[0]]=1
else:
    DP[0][L[0]]=1

for i in range(1,n):
    for j in range(100000*20,-100000*20-1, -1):
        if -100000*20<=j-L[i] and j-L[i]<=100000*20:
            if j-L[i]<0:
                if j<0 and NP[i-1][-(j-L[i])]:
                    NP[i][-j]+=NP[i-1][-(j-L[i])]
                    #print(f'NP[{-(j+L[i])}]+=NP[{-j}]')
                    #time.sleep(1)
                elif j<0:
                    NP[i][-j]=NP[i-1][-j]
                elif j>=0 and NP[i-1][-(j-L[i])]:
                    DP[i][j]+=NP[i-1][-(j-L[i])]
                    #print(f'DP[{j+L[i]}]+=NP[{-j}]')
                    #time.sleep(1)
                else:
                    DP[i][j]=DP[i-1][j]         
            else:
                if j<0 and DP[i-1][(j-L[i])]:
                    NP[i][-j]+=DP[i-1][(j-L[i])]
                    #print(f'NP[{-(j+L[i])}]+=NP[{-j}]')
                    #time.sleep(1)
                elif j<0:
                    NP[i][-j]=NP[i-1][-j]
                elif j>=0 and DP[i-1][(j-L[i])]:
                    DP[i][j]+=DP[i-1][(j-L[i])]
                    #print(f'DP[{j+L[i]}]+=NP[{-j}]')
                    #time.sleep(1)
                else:
                    DP[i][j]=DP[i-1][j]     
'''
for i in range(-100000*20, 1):
    if NP[i]:
        print(i, NP[i])
for i in range(100000*20+1):
    if DP[i]:
        print(i, DP[i])     
'''
DP[n-1][0]-=1
if s<0:
    print(NP[n-1][-s])
else:
    print(DP[n-1][s])

