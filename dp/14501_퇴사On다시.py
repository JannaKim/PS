N = int(input())
# cn: consult
cn=[[0,0]]
for _ in range(N):
    cn.append([int(i) for i in input().split()])

# dp[i][0]: i일전까지 일했을 때 얻을 수 있는 최대 수익
# dp[i][1]: 최대수익의 시작일

dp=[[]]*(N+1)
L=[0]*(N+1)
for i in range(1,N+1):
        L[i] = cn[i][1]
link=[]
for _ in range(N+1):
    link.append([])

for i in range(1,N+1):
    if i+cn[i][0]<N+1:
        link[i+cn[i][0]].append(i)

print(link)
for i in range(1,N+1):
    for j in link[i]:
        print(f'j={j}')
        if j-1>0:
            dp[i]+=[[cn[j][1],j-1]]
print(dp)